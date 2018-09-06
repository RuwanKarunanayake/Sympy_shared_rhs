// generated by bssnUtils.py code for derivative computation
//date: 2018-09-06 17:58:48
#ifndef BSSN_RHS_DERIV_COMP 
#define BSSN_RHS_DERIV_COMP
#include<iostream>
#include"cuda_runtime.h"
#include<device_launch_parameters.h>
#include "block_cu.h"
#include "params_cu.h"
#include "bssn_rhs_deriv_mem_cuda.h"
#include "cudaUtils.cuh"
#include "derivs.cuh"
namespace cuda {

/**compute derivative kernel __computeDerivPass1*/
__global__ void __computeDerivPass1(const double**__unzipInVar,MemoryDerivs* __derivWorkspace, const cuda::_Block* __dendroBlkList, const cudaDeviceProp* __deviceProperties);

/**compute derivative kernel __computeDerivPass2*/
__global__ void __computeDerivPass2(const double**__unzipInVar,MemoryDerivs* __derivWorkspace, const cuda::_Block* __dendroBlkList, const cudaDeviceProp* __deviceProperties);

/**compute derivative kernel __computeDerivPass3*/
__global__ void __computeDerivPass3(const double**__unzipInVar,MemoryDerivs* __derivWorkspace, const cuda::_Block* __dendroBlkList, const cudaDeviceProp* __deviceProperties);

/**compute derivative kernel __computeDerivPass4*/
__global__ void __computeDerivPass4(const double**__unzipInVar,MemoryDerivs* __derivWorkspace, const cuda::_Block* __dendroBlkList, const cudaDeviceProp* __deviceProperties);

/**compute derivative kernel __computeDerivPass5*/
__global__ void __computeDerivPass5(const double**__unzipInVar,MemoryDerivs* __derivWorkspace, const cuda::_Block* __dendroBlkList, const cudaDeviceProp* __deviceProperties);

}// end of namespace cuda


#endif
