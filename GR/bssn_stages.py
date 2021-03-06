####################################################################
# May.8.2018
# Adding gamma driver into shift equation to optimize BBH behavior
# with large mass ratio
#####################################################################
import dendro
from sympy import *
from sympy.physics.vector.vector import Vector
from sympy.printing.dot import dotprint

import bssnUtils as utils
###################################################################
# initialize
###################################################################

l1, l2, l3, l4, eta = symbols('lambda[0] lambda[1] lambda[2] lambda[3] eta')
lf0, lf1 = symbols('lambda_f[0] lambda_f[1]')

# Additional parameters for damping term
R0 = symbols('R0')
ep1, ep2 = symbols('eta_power[0] eta_power[1]')


# declare variables
a   = dendro.scalar("alpha", "[pp]")
chi = dendro.scalar("chi", "[pp]")
K   = dendro.scalar("K", "[pp]")

Gt  = dendro.vec3("Gt", "[pp]")
b   = dendro.vec3("beta", "[pp]")
B   = dendro.vec3("B", "[pp]")

gt  = dendro.sym_3x3("gt", "[pp]")
At  = dendro.sym_3x3("At", "[pp]")


# note: these are just the symbolic vars that is being used to generate the
# Gt_rhs by satges

_Gt_rhs_s1  = dendro.vec3("Gt_rhs_s1_", "[pp]")
_Gt_rhs_s2  = dendro.vec3("Gt_rhs_s2_", "[pp]")
_Gt_rhs_s3  = dendro.vec3("Gt_rhs_s3_", "[pp]")
_Gt_rhs_s4  = dendro.vec3("Gt_rhs_s4_", "[pp]")
_Gt_rhs_s5  = dendro.vec3("Gt_rhs_s5_", "[pp]")
_Gt_rhs_s6  = dendro.vec3("Gt_rhs_s6_", "[pp]")
_Gt_rhs_s7  = dendro.vec3("Gt_rhs_s7_", "[pp]")
_CalGt  = dendro.vec3("CalGt", "[pp]")
_Gt_rhs  = dendro.vec3("Gt_rhs", "[pp]")


# Gt_rhs staged vars that is being used to generate the code.
At_UU  = dendro.sym_3x3("At_UU", "[pp]")
CalGt  = dendro.vec3("CalGt", "[pp]")
Gt_rhs_s1  = dendro.vec3("Gt_rhs_s1_", "[pp]")
Gt_rhs_s2  = dendro.vec3("Gt_rhs_s2_", "[pp]")
Gt_rhs_s3  = dendro.vec3("Gt_rhs_s3_", "[pp]")
Gt_rhs_s4  = dendro.vec3("Gt_rhs_s4_", "[pp]")
Gt_rhs_s5  = dendro.vec3("Gt_rhs_s5_", "[pp]")
Gt_rhs_s6  = dendro.vec3("Gt_rhs_s6_", "[pp]")
Gt_rhs_s7  = dendro.vec3("Gt_rhs_s7_", "[pp]")

Gt_rhs  = dendro.vec3("Gt_rhs", "[pp]")

# Lie derivative weight
weight = -Rational(2,3)
weight_Gt = Rational(2,3)

# specify the functions for computing first and second derivatives
d = dendro.set_first_derivative('grad')    # first argument is direction
d2s = dendro.set_second_derivative('grad2')  # first 2 arguments are directions
ad = dendro.set_advective_derivative('agrad')  # first argument is direction
kod = dendro.set_kreiss_oliger_dissipation('kograd')

d2 = dendro.d2

#f = Function('f')

# generate metric related quantities
dendro.set_metric(gt)
igt = dendro.get_inverse_metric()

C1 = dendro.get_first_christoffel()
C2 = dendro.get_second_christoffel()
C2_spatial = dendro.get_complete_christoffel(chi)
R, Rt, Rphi, CalGt = dendro.compute_ricci(Gt, chi)
###################################################################
# evolution equations
###################################################################

a_rhs = l1*dendro.lie(b, a) - 2*a*K + 0*dendro.kodiss(a)


b_rhs = [ S(3)/4 * (lf0 + lf1*a) * B[i] +
        l2 * dendro.vec_j_ad_j(b, b[i])
         for i in dendro.e_i ] + 0*dendro.kodiss(b)

gt_rhs = dendro.lie(b, gt, weight) - 2*a*At + 0*dendro.kodiss(gt)

chi_rhs = dendro.lie(b, chi, weight) + Rational(2,3) * (chi*a*K) + 0*dendro.kodiss(chi)

AikAkj = Matrix([sum([At[i, k] * sum([dendro.inv_metric[k, l]*At[l, j] for l in dendro.e_i]) for k in dendro.e_i]) for i, j in dendro.e_ij])

At_rhs = dendro.lie(b, At, weight) + chi*dendro.trace_free( a*R - dendro.DiDj(a)) + a*(K*At - 2*AikAkj.reshape(3, 3)) + 0*dendro.kodiss(At)

K_rhs = dendro.lie(b, K) - dendro.laplacian(a,chi) + a*(K*K/3 + dendro.sqr(At)) + 0*dendro.kodiss(K)

At_UU = dendro.up_up(At)

Gt_rhs_s1= ([sum(b[j]*ad(j,Gt[i]) for j in dendro.e_i) for i in dendro.e_i])
Gt_rhs_s2= ([sum(_CalGt[j]*d(j,b[i]) for j in dendro.e_i) for i in dendro.e_i])
Gt_rhs_s3= ([ _CalGt[i] * sum(d(j,b[j]) for j in dendro.e_i)  for i in dendro.e_i ])
Gt_rhs_s4= ([sum([igt[j, k] * d2(j, k, b[i]) + igt[i, j] * d2(j, k, b[k])/3 for j, k in dendro.e_ij]) for i in dendro.e_i])
Gt_rhs_s5= ([sum([2*At_UU[i, j]*d(j, a) for j in dendro.e_i]) for i in dendro.e_i])
Gt_rhs_s6= ([sum([2*a*dendro.C2[i, j, k]*At_UU[j, k] for j,k in dendro.e_ij]) for i in dendro.e_i])
Gt_rhs_s7= ([sum([a*(3/chi*At_UU[i,j]*d(j, chi) + Rational(4,3)*dendro.inv_metric[i, j]*d(j, K)) for j in dendro.e_i]) for i in dendro.e_i])

'''Gt_rhs = Matrix([sum(b[j]*ad(j,Gt[i]) for j in dendro.e_i) for i in dendro.e_i]) - \
         Matrix([sum(CalGt[j]*d(j,b[i]) for j in dendro.e_i) for i in dendro.e_i]) + \
         Rational(2,3)*Matrix([ CalGt[i] * sum(d(j,b[j]) for j in dendro.e_i)  for i in dendro.e_i ]) + \
         Matrix([sum([igt[j, k] * d2(j, k, b[i]) + igt[i, j] * d2(j, k, b[k])/3 for j, k in dendro.e_ij]) for i in dendro.e_i]) - \
         Matrix([sum([2*At_UU[i, j]*d(j, a) for j in dendro.e_i]) for i in dendro.e_i]) + \
         Matrix([sum([2*a*dendro.C2[i, j, k]*At_UU[j, k] for j,k in dendro.e_ij]) for i in dendro.e_i]) - \
         Matrix([sum([a*(3/chi*At_UU[i,j]*d(j, chi) + Rational(4,3)*dendro.inv_metric[i, j]*d(j, K)) for j in dendro.e_i]) for i in dendro.e_i])
         # + kod(i,Gt[i])'''


Gt_rhs = Matrix(_Gt_rhs_s1) - \
         Matrix(_Gt_rhs_s2) + \
         Rational(2,3)*Matrix(_Gt_rhs_s3) + \
         Matrix(_Gt_rhs_s4) - \
         Matrix(_Gt_rhs_s5) + \
         Matrix(_Gt_rhs_s6) - \
         Matrix(_Gt_rhs_s7)



# + kod(i,Gt[i])


Gt_rhs = [item for sublist in Gt_rhs.tolist() for item in sublist]

eta_func = R0*sqrt(sum([igt[i,j]*d(i,chi)*d(j,chi) for i,j in dendro.e_ij]))/((1-chi**ep1)**ep2)

B_rhs = [_Gt_rhs[i] - eta_func * B[i] +
         l3 * dendro.vec_j_ad_j(b, B[i]) -
         l4 * dendro.vec_j_ad_j(b, Gt[i]) + 0*kod(i,B[i])
         for i in dendro.e_i]

outs = [a_rhs, b_rhs, gt_rhs, chi_rhs, At_rhs, K_rhs, CalGt, Gt_rhs_s1, Gt_rhs_s2, Gt_rhs_s3, Gt_rhs_s4, Gt_rhs_s5, Gt_rhs_s6, Gt_rhs_s7, Gt_rhs, B_rhs]
vnames = ['a_rhs', 'b_rhs', 'gt_rhs', 'chi_rhs', 'At_rhs', 'K_rhs', 'CalGt', 'Gt_rhs_s1_', 'Gt_rhs_s2_', 'Gt_rhs_s3_', 'Gt_rhs_s4_', 'Gt_rhs_s5_', 'Gt_rhs_s6_', 'Gt_rhs_s7_', 'Gt_rhs', 'B_rhs']

# outs = [a_rhs, b_rhs, gt_rhs, chi_rhs, K_rhs, CalGt, Gt_rhs_s1, Gt_rhs_s2, Gt_rhs_s3, Gt_rhs_s4, Gt_rhs_s5, Gt_rhs_s6, Gt_rhs_s7, Gt_rhs, B_rhs]
# vnames = ['a_rhs', 'b_rhs', 'gt_rhs', 'chi_rhs', 'K_rhs', 'CalGt', 'Gt_rhs_s1_', 'Gt_rhs_s2_', 'Gt_rhs_s3_', 'Gt_rhs_s4_', 'Gt_rhs_s5_', 'Gt_rhs_s6_', 'Gt_rhs_s7_', 'Gt_rhs', 'B_rhs']


# outs = [ CalGt, Gt_rhs_s1, Gt_rhs_s2, Gt_rhs_s3, Gt_rhs_s4, Gt_rhs_s5, Gt_rhs_s6, Gt_rhs_s7, Gt_rhs, B_rhs]
# vnames = ['CalGt', 'Gt_rhs_s1_', 'Gt_rhs_s2_', 'Gt_rhs_s3_', 'Gt_rhs_s4_', 'Gt_rhs_s5_', 'Gt_rhs_s6_', 'Gt_rhs_s7_', 'Gt_rhs', 'B_rhs']

#Genrate  code using ComputeRHSSourceUnstaged method in bssnUtils
# utils.cudaComputeRHSSourceUnStaged("rhs_unstaged.cu",outs,vnames)
utils.cudaComputeRHSSourceUnStaged_thread_No_preserved("rhs_unstaged_const_threadNo.cu",outs,vnames)