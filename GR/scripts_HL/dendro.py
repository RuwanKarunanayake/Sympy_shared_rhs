##########################################################################
# module: dendro
# author: Hari Sundar
# email:  hari@cs.utah.edu
#
# python module to generate efficient code for General Relativity.
#
# (c) 2016 University of Utah, All rights reserved.
##########################################################################

from sympy import *
from sympy.tensor.array import *
from sympy.functions.special.tensor_functions import KroneckerDelta
from sympy.utilities import numbered_symbols
from sympy.printing import print_ccode

import string
import random

# internal variables
undef = symbols('undefined')

metric = undef
inv_metric = undef
C1 = undef
C2 = undef
# C2_spatial
C3 = undef

# first derivative
d = undef
# second derivative
d2 = undef
# advective derivative
ad = undef

e_i = [0, 1, 2]
e_ij = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

Ricci = undef

##########################################################################
# variable initialization functions
##########################################################################


def scalar(name):
    """
    Create a scalar variable with the corresponding name. The 'name' will be during code generation, so should match the
    variable name used in the C++ code.
    """
    return symbols(name)


def vec3(name):
    """
    Create a 3D vector variable with the corresponding name. The 'name' will be during code generation, so should match
    the variable name used in the C++ code. The returned variable can be indexed(0,1,2), i.e.,

    b = dendro.vec3("beta")
    b[1] = x^2
    """
    vname = ' '.join([name + repr(i) for i in [0, 1, 2]])
    return symbols(vname)


def sym_3x3(name):
    """
    Create a symmetric 3x3 matrix variables with the corresponding name. The 'name' will be during code generation, so
    should match the variable name used in the C++ code. The returned variable can be indexed(0,1,2)^2, i.e.,

    gt = dendro.sym_3x3("gt")
    gt[0,2] = x^2
    """

    vname = ' '.join([name + repr(i) for i in range(6)])
    m1, m2, m3, m4, m5, m6 = symbols(vname)

    return Matrix([[m1, m2, m3], [m2, m4, m5], [m3, m5, m6]])


##########################################################################
# derivative related functions
##########################################################################


def set_first_derivative(g):
    """
    Set how the stencil for the first derivative will be called. Here g is a string

    Typically,

    d_i u =  g(i, u)
    """
    global d
    d = Function(g)
    return d


def set_second_derivative(g):
    """
    Set how the stencil for the second derivative will be called. Here g is a string

    Typically,

    d_ij u =  g(i, j, u)
    """
    global d2
    d2 = Function(g)
    return d2

def set_advective_derivative(g):
    """
    Set how the stencil for the second derivative will be called. Here g is a string

    Typically,

    ad_i u =  g(i, u)
    """
    global ad
    ad = Function(g)
    return ad



# Covariant Derivatives
def DiDj(a):
    """
    Defines the covariant derivative for a scalar a with respect to the full metric.
    [ewh] Actually this defines two covariant derivatives acting on a scalar.   
    The derivative in this case is built from the full (non-conformal) metric.
    Thus C3 is built from the full metric.  This object is symmetric in both 
    indices.  
    """
    global d, d2, C3

    m = Matrix([d2(i, j, a) - sum([C3[l, i, j] * d(l, a) for l in e_i]) for i, j in e_ij])
    return m.reshape(3, 3)


def _Di_Dj(a):
    """
    Defines the covariant derivative. 
    [ewh]  Actually, this defines two covariant derivatives acting on a scalar.
    The use of C2 below, however, suggests that this derivative is built
    from the conformal metric.  Such an operator and term shows up in the 
    definition of the Ricci scalar which, in turn shows up in the trace-free 
    term in the At evolution equation.  As with DiDj, this object is symmetric 
    in both indices when acting on a scalar.  
    """
#[ewh] shouldn't this be C2 instead of C3, i.e.:
    global d, d2, C2
#    global d, d2, C3

    m = Matrix([d2(i, j, a) - sum([C2[l, i, j] * d(l, a) for l in e_i]) for i, j in e_ij])
    return m.reshape(3, 3)


# Index Raising
def up_up(A):
    """
    raises both the indices of A, i.e., A_{ij} --> A^{ij}
    """
    global inv_metric

    m = Matrix([sum([inv_metric[i, k]*inv_metric[j, l]*A[k, l] for k, l in e_ij]) for i, j in e_ij])
    return m.reshape(3, 3)


def lie(b, a, weight=0):
    """
    Computes the Lie derivative of a field, a, along the vector b.  Assumes 
    the metric has been set.  An optional weight for the field can be 
    specified.

    b must be of type dendro.vec3
    a can be scalar, vec3 or sym_3x3

    Computes L_b(v)
    """
    global d, ad

    # e_ij = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

    if type(b) != tuple:
        raise ValueError('Dendro: The field wrt which the Lie derivative is calculated needs to be vec3.')

    if type(a) == Symbol:
        return sum([b[i] * ad(i, a) for i in e_i]) + weight*a*sum([d(i, b[i]) for i in e_i])
    elif type(a) == tuple:
        return [sum([b[j] * ad(j, a[i]) - a[j] * d(j, b[i]) + weight*a[i]*d(j, b[j]) for j in e_i]) for i in e_i]
    elif type(a) == Matrix:
        m = Matrix([sum([b[k]*ad(k, a[i, j]) + a[i, k]*d(j, b[k]) + a[k, j]*d(i, b[k]) + weight*a[i, j]*d(k, b[k]) for k in e_i]) for i, j in e_ij])
        return m.reshape(3, 3)
    else:
        raise ValueError('Dendro: Unknown type for input field to compute Lie derivative for.')


def laplacian(a, chi):
    """
    Computes the laplacian of a scalar function with respect to the 3D metric
    gamma_ij.  Assumes that the conformally rescaled metric (called gt in 
    various places) and the conformal factor (chi) is set.  Note that C3 is 
    built from the same 3D metric.  The only place that this laplacian is
    used in the bssn equations is in the evolution equation for K and is
    the laplacian of alpha (the lapse).  
    """
    global d, d2, metric, C3

    full_metric = metric/chi
    inv_full_metric = simplify(full_metric.inv('ADJ'))

#    return sum([(inv_full_metric[i, j] * d2(i, j, a) - sum([C3[l, i, j] * d(l, a) for l in e_i])) for i, j in e_ij])
    return sum([ inv_full_metric[i, j] * ( d2(i, j, a) - sum([C3[l, i, j] * d(l, a) for l in e_i]) ) for i, j in e_ij])


def laplacian_conformal(a):
    """
    Computes the (conformal) laplacian of a scalar function with respect 
    to the tilded or conformally rescaled metric (called gt in various 
    places).  We assume the rescaled metric is set as well the conformal
    factor, chi.  Note that C2 is built from the conformally rescaled 
    metrci.  This (conformal) laplacian is only used in the definition of 
    Ricci that shows up in the evolution equation for At (under the trace
    free operation), and even then only in the part that multiplies the 
    metric and which will drop out on taking the trace free part.  So, in 
    fact, the code could be written to completely ignore this operation
    in the evolution equations themselves.  However, if the constraints 
    are included or the full Ricci is needed for another reason, this 
    would be needed.  
    """
    global d, d2, inv_metric, C2

    if inv_metric == undef:
        inv_metric = get_inverse_metric()

#ewh3    return sum([(inv_metric[i, j] * d2(i, j, a) - sum([C2[l, i, j] * d(l, a) for l in e_i])) for i, j in e_ij])
    return sum([ inv_metric[i, j] * (d2(i, j, a) - sum([C2[l, i, j] * d(l, a) for l in e_i])) for i, j in e_ij])


def sqr(a):
    """
    Computes the square of the matrix. Assumes metric is set.
    """
    global inv_metric

    if inv_metric == undef:
        inv_metric = get_inverse_metric()

    return sum([a[i, j]*sum([inv_metric[i, k] * inv_metric[j, l] * a[k, l] for k in e_i for l in e_i]) for i, j in e_ij])


def trace_free(x):
    """
    makes the operator trace-free
    """
    global metric, inv_metric

    if inv_metric == undef:
        inv_metric = get_inverse_metric()

    trace = sum([ inv_metric[i, j] * x[i, j] for i, j in e_ij])

    # X_{ab} - 1/3 gt_{ab} X.
#    tf = Matrix([x[i, j] - 1/3*metric[i,j]*trace for i, j in e_ij])
    tf = Matrix([x[i, j] - metric[i,j]*trace/3 for i, j in e_ij])

    return tf.reshape(3, 3)

def vec_j_del_j(b, a):
    """
    expands to  $\beta^i\partial_i \alpha$
    """
    return sum([b[i]*d(i, a) for i in e_i])


#[ewh] Adding this as this term needs to be in the beta equation as an 
#      advective derivative ... and not as a regular (partial) derivative.      
def vec_j_ad_j(b, f):
    """
    expands to  $\beta^i\partial_i f$
    """
    return sum([b[i]*ad(i, f) for i in e_i])

#vec_k_del_k = vec_j_del_j

##########################################################################
# metric related functions
##########################################################################


def set_metric(g):
    """
    sets the metric variable, so that dendro knows how to compute the derived variables. This should be done fairly
    early on. e.g.,

    gt = dendro.sym_3x3("gt")
    dendro.set_metric(gt)
    """
    global metric

    metric = g


def get_inverse_metric():
    """
    Computes and returns the inverse metric. The variables need for be defined in advance. e.g.,

    gt = dendro.sym_3x3("gt")
    dendro.set_metric(gt)
    igt = dendro.get_inverse_metric()
    """
    global metric, inv_metric, undef

    if metric == undef:
        raise ValueError('Dendro: Metric not defined.')

    if inv_metric == undef:
        # method : ('GE', 'LU', or 'ADJ')
        inv_metric = simplify(metric.inv('ADJ'))

    return inv_metric


def get_first_christoffel():
    """
    Computes and returns the first Christoffel Symbols. Assumes the metric has been set. e.g.,

    dendro.set_metric(gt);

    C1 = dendro.get_first_christoffel();
    """
    global metric, inv_metric, undef, C1, d

    if inv_metric == undef:
        get_inverse_metric()

    if C1 == undef:
        C1 = MutableDenseNDimArray(range(27), (3, 3, 3))

        for k in e_i:
            for j in e_i:
                for i in e_i:
#                    C1[k, i, j] = 1 / 2 * (d(j, metric[k, i]) + d(i, metric[k, j]) - d(k, metric[i, j]))
                    C1[k, i, j] = 0.5 * (d(j, metric[k, i]) + d(i, metric[k, j]) - d(k, metric[i, j]))

    return C1


def get_second_christoffel():
    """
    Computes and returns the second Christoffel Symbols. Assumes the metric has been set. Will compute the first
    Christoffel if not already computed. e.g.,

    dendro.set_metric(gt);

    C2 = dendro.get_second_christoffel();
    """
    global C2, C1, inv_metric

    if C2 == undef:
        if C1 == undef:
            get_first_christoffel()

        igt_t = Array(inv_metric, (3, 3))
        C2 = tensorcontraction(tensorproduct(igt_t, C1), (1, 2))

    return C2


def get_complete_christoffel(chi):
    """
    Computes and returns the second Christoffel Symbols. Assumes the metric has been set. Will compute the first/second
    Christoffel if not already computed. e.g.,

    dendro.set_metric(gt);

    C2_spatial = dendro.get_complete_christoffel();
    """
    global metric, inv_metric, undef, C1, C2, C3, d

    if C3 == undef:
        C3 = MutableDenseNDimArray(range(27), (3, 3, 3))

        if C2 == undef:
            get_second_christoffel()

        for k in e_i:
            for j in e_i:
                for i in e_i:
#                    C3[i, j, k] = C2[i, j, k] - 1/(2*chi)*(KroneckerDelta(i, j) * d(k, chi) +
                    C3[i, j, k] = C2[i, j, k] - 0.5/(chi)*(KroneckerDelta(i, j) * d(k, chi) +
                                                           KroneckerDelta(i, k) * d(j, chi) -
                                                           metric[j, k]*sum([inv_metric[i, m]*d(m, chi) for m in e_i])
                                                           )

    return C3


def compute_ricci(Gt, chi):
    """
    Computes the Ricci tensor. e.g.,

    dendro.set_metric(gt)

    R = dendro.compute_ricci(Gt, chi)

    or

    dendro.compute_ricci(Gt, chi)

    and use

    dendro.ricci

    The conformal connection coefficient and the conformal variable needs to be supplied.
    """
    global metric, inv_metric, C1, C2, d2

    Lchi = laplacian_conformal(chi)

    #print(type(Lchi))

    #print('Done with Lphi') #simplify(Lchi))


#ewh4    DKchiDkchi = Matrix([4*metric[i, j]*sum([sum([inv_metric[k, l]*d(l, chi) for l in e_i])*d(k, chi) for k in e_i]) for i, j in e_ij])
    DKchiDkchi = Matrix([0.25/chi/chi*metric[i, j]*sum([sum([inv_metric[k, l]*d(l, chi) for l in e_i])*d(k, chi) for k in e_i]) for i, j in e_ij])

    #print('done with DKchi') # simplify(DKchiDkchi))

    CalGt = [sum(inv_metric[k,l]*C2[i,k,l] for k, l in e_ij) for i in e_i]

    Rt = Matrix([-0.5*sum([inv_metric[l, m]*d2(l, m, metric[i, j]) for l, m in e_ij]) +
              0.5*sum([metric[k,i]*d(j, Gt[k]) + metric[k,j]*d(i, Gt[k]) for k in e_i]) +
              0.5*sum([CalGt[k]*(C1[i,j,k] + C1[j,i,k]) for k in e_i]) +
              sum([inv_metric[l,m]*(C2[k,l,i]*C1[j,k,m] + C2[k,l,j]*C1[i,k,m] + C2[k,i,m]*C1[k,l,j])
                   for k in e_i for l,m in e_ij]) for i,j in e_ij])

    #print('done with Rt') #simplify(Rt))

#ewh5    Rphi_tmp = Matrix([2*metric[i, j]*Lchi - 4*d(i, chi)*d(j, chi) for i, j in e_ij])
#dwn    Rphi_tmp = Matrix([ 0.5*metric[i, j]*Lchi/chi - 0.25*d(i, chi)*d(j, chi)/chi/chi for i, j in e_ij])

    #print(simplify(Rphi_tmp))

#ewh6    Rphi = -2*_Di_Dj(chi) - Rphi_tmp.reshape(3, 3) - DKchiDkchi.reshape(3, 3)
#dwn    Rphi = -0.5*_Di_Dj(chi)/chi - Rphi_tmp.reshape(3, 3) - DKchiDkchi.reshape(3, 3)
    xRphi = Matrix( [ 1/(2*chi)*(d2(i,j,chi) - 
          sum(C2[k,j,i]*d(k,chi) for k in e_i)) -
          1/(4*chi*chi)*d(i,chi)*d(j,chi) for i, j in e_ij]).reshape(3,3)

    Rphi = xRphi + Matrix( [ 
           1/(2*chi)*metric[i,j] * ( sum(inv_metric[k,l]*(d2(k,l,chi) - 
           3/(2*chi)*d(k,chi)*d(l,chi))  for k, l in e_ij) - 
           sum(CalGt[m]*d(m,chi) for m in e_i))
           for i, j in e_ij ] ).reshape(3,3)

    return [Rt.reshape(3, 3) + Rphi, Rt.reshape(3,3), Rphi, CalGt]

##########################################################################
# code generation function
##########################################################################


def generate(ex, vnames):
    """
    Generate the C++ code by simplifying the expressions.
    """
    # print(ex)

    mi = [0, 1, 2, 4, 5, 8]
    midx = ['00', '01', '02', '11', '12', '22']

    # total number of expressions
    # print("--------------------------------------------------------")
    num_e = 0
    lexp = []
    lname = []
    for i, e in enumerate(ex):
        if type(e) == list:
            num_e = num_e + len(e)
            for j, ev in enumerate(e):
                lexp.append(ev)
                lname.append(vnames[i]+repr(j))
        elif type(e) == Matrix:
            num_e = num_e + len(e)
            for j, k in enumerate(mi):
                lexp.append(e[k])
                lname.append(vnames[i]+midx[j])
        else:
            num_e = num_e + 1
            lexp.append(e)
            lname.append(vnames[i])

    # print(num_e)
    # print(len(lname))

    print('// Dendro: {{{ ')
    print('// Dendro: original ops: ', count_ops(lexp))

    # print("--------------------------------------------------------")
    # print("Now trying Common Subexpression Detection and Collection")
    # print("--------------------------------------------------------")

    # Common Subexpression Detection and Collection
    # for i in range(len(ex)):
    #     # print("--------------------------------------------------------")
    #     # print(ex[i])
    #     # print("--------------------------------------------------------")
    #     ee_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    #     ee_syms = numbered_symbols(prefix=ee_name)
    #     _v = cse(ex[i],symbols=ee_syms)
    #     # print(type(_v))
    #     for (v1,v2) in _v[0]:
    #         print("double %s = %s;" % (v1, v2))
    #     print("%s = %s" % (vnames[i], _v[1][0]))
  
    #mex = Matrix(ex)
    ee_name = 'DENDRO_' #''.join(random.choice(string.ascii_uppercase) for _ in range(5))
    ee_syms = numbered_symbols(prefix=ee_name)
    _v = cse(lexp, symbols=ee_syms, optimizations='basic')

    custom_functions = {'grad': 'grad', 'grad2': 'grad2', 'agrad': 'agrad'}

    rops=0
    print('// Dendro: printing temp variables')
    for (v1, v2) in _v[0]:
        # print("double %s = %s;" % (v1, v2)) # replace_pow(v2)))
        print('double ', end='')
        print_ccode(v2, assign_to=v1, user_functions=custom_functions)
        rops = rops + count_ops(v2)

    print()
    print('// Dendro: printing variables')
    for i, e in enumerate(_v[1]):
        print("//--")
        # print("%s = %s;" % (lname[i], e)) # replace_pow(e)))
        print_ccode(e, assign_to=lname[i], user_functions=custom_functions)
        rops = rops + count_ops(e)

    print('// Dendro: reduced ops: ', rops)
    print('// Dendro: }}} ')

def replace_pow(exp_in):
    """
    Convert integer powers in an expression to Muls, like a**2 => a*a
    :param exp_in: the input expression,
    :return: the output expression with only Muls
    """
    pows = list(exp_in.atoms(Pow))
    if any(not e.is_Integer for b, e in (i.as_base_exp() for i in pows)):
         raise ValueError("Dendro: Non integer power encountered.")
    repl = zip(pows, (Mul(*[b]*e, evaluate=False) for b, e in (i.as_base_exp() for i in pows)))
    return exp_in.xreplace(dict(repl))


def generate_debug (ex, vnames):
    """
    Generate the C++ code by simplifying the expressions.
    """
    # print(ex)

    mi = [0, 1, 2, 4, 5, 8]
    midx = ['00', '01', '02', '11', '12', '22']

    # total number of expressions
    # print("--------------------------------------------------------")
    num_e = 0
    lexp = []
    lname = []
    print('// Dendro: {{{ ')
    for i, e in enumerate(ex):
        if type(e) == list:
            num_e = num_e + len(e)
            for j, ev in enumerate(e):
                # lexp.append(ev)
                print(vnames[i] + repr(j), end='')
                print(' = ', end='')
                print(replace_pow(ev), ';')
        elif type(e) == Matrix:
            num_e = num_e + len(e)
            for j, k in enumerate(mi):
                # lexp.append(e[k])
                print(vnames[i] + midx[j], end='')
                print(' = ', end='')
                print(replace_pow(e[k]), ';')
        else:
            num_e = num_e + 1
            #lexp.append(e)
            print(vnames[i], end='')
            print(' = ', end='')
            print(replace_pow(e), ';')

    print('// Dendro: }}} ')
