# SymPyGR 
SymPy based framework for optimized code generation for BSSN formulation of Einstein equation for heterogeneous platforms. 

Dendro is an adaptive meshing framework that enables solving large-scale
computational problems on octree-refined meshes. The cu rrent vers ion of dendro and
dendro_sym , handle adaptivity by decomposing the domain into a collection of small
regular blocks (uniformly refined), on which the code corresponding to the PDE are
automatically generated (C/C++) from the symbolic expressions. While the overall
framework works cu rrently, there are several areas for improving per formance and
portability and these are the possible research topics. Note that although dendro
supports distributed computing on large clusters, these improvements are only
required at the single-node and possibly single-thread level, as the blocks generated by
dendro are typically 16^3 to 256^3 in size. The topics listed below are tagged with the key
focus areas, gpu, openmp , simd, graph. 

* graph: Sympy produces an expression tree that is sufficiently simplified. But,
there are several repeated expressions within this tree that can be simplified by
factoring out these expressions and evaluating them only once. The main focus of
this task would be to develop algorithms for extracting common sub-expressions
within sympy. This would most likely be done in python.
* openmp, gpu Dendro produces a list of blocks that need to be scheduled across
threads and GPUs. We cu rrently support simple scheduling via openmp.
Performance and load-balancing can be improved significantly by better
scheduling of the blocks. Of particular interest is to device methods to scheduled
blocks dynamically between GPUs and CPUs. This might ha ve to be done in C/C++
to schedule the blocks. This C++ code can potentially be autogenerated from the
python code.
* gpu, simd As previously mentioned, the cu rrent implementation generates C++
code from the sympy expression trees. A very important contribution would be to
add python code to generate for different architectu re targets, such as
1. default: pure C/C++ code
2. avx2: SIMD code targeting 256-bit wide AVX2 architectu res
3. avx512: SIMD code targeting 512-bit wide architectu res, such as the Xeon PH I
4. cuda: CUDA code targeting nVidia GPUs, possibly with options targeting
different generations.
5. openCL, openACC : and others.
