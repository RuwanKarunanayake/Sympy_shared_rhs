// generated code for derivative allocations and deallocations 
//date: 2018-09-06 14:54:50
#include "bssn_rhs_deriv_mem_cuda.h"

namespace cuda {


	/**@brief memory allocation for deriv variables */
	void cuda::MemoryDerivs::allocateDerivMemory(unsigned int maxBlkSz){ 
		 __maxBlkSz=maxBlkSz;
		 const size_t bytes=sizeof(double)*__maxBlkSz;
		 cudaMalloc((void **)&__grad_0_alpha,bytes);
		 cudaMalloc((void **)&__grad_1_alpha,bytes);
		 cudaMalloc((void **)&__grad_2_alpha,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt0,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt0,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt0,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt0,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt0,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt0,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt1,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt1,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt1,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt1,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt1,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt1,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt2,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt2,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt2,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt2,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt2,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt2,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt3,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt3,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt3,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt3,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt3,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt3,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt4,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt4,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt4,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt4,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt4,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt4,bytes);
		 cudaMalloc((void **)&__grad2_0_0_gt5,bytes);
		 cudaMalloc((void **)&__grad2_0_1_gt5,bytes);
		 cudaMalloc((void **)&__grad2_0_2_gt5,bytes);
		 cudaMalloc((void **)&__grad2_1_1_gt5,bytes);
		 cudaMalloc((void **)&__grad2_1_2_gt5,bytes);
		 cudaMalloc((void **)&__grad2_2_2_gt5,bytes);
		 cudaMalloc((void **)&__grad2_0_0_chi,bytes);
		 cudaMalloc((void **)&__grad2_0_1_chi,bytes);
		 cudaMalloc((void **)&__grad2_0_2_chi,bytes);
		 cudaMalloc((void **)&__grad2_1_1_chi,bytes);
		 cudaMalloc((void **)&__grad2_1_2_chi,bytes);
		 cudaMalloc((void **)&__grad2_2_2_chi,bytes);
		 cudaMalloc((void **)&__grad2_0_0_alpha,bytes);
		 cudaMalloc((void **)&__grad2_0_1_alpha,bytes);
		 cudaMalloc((void **)&__grad2_0_2_alpha,bytes);
		 cudaMalloc((void **)&__grad2_1_1_alpha,bytes);
		 cudaMalloc((void **)&__grad2_1_2_alpha,bytes);
		 cudaMalloc((void **)&__grad2_2_2_alpha,bytes);
		 cudaMalloc((void **)&__grad2_0_0_beta0,bytes);
		 cudaMalloc((void **)&__grad2_0_1_beta0,bytes);
		 cudaMalloc((void **)&__grad2_0_2_beta0,bytes);
		 cudaMalloc((void **)&__grad2_1_1_beta0,bytes);
		 cudaMalloc((void **)&__grad2_1_2_beta0,bytes);
		 cudaMalloc((void **)&__grad2_2_2_beta0,bytes);
		 cudaMalloc((void **)&__grad2_0_0_beta1,bytes);
		 cudaMalloc((void **)&__grad2_0_1_beta1,bytes);
		 cudaMalloc((void **)&__grad2_0_2_beta1,bytes);
		 cudaMalloc((void **)&__grad2_1_1_beta1,bytes);
		 cudaMalloc((void **)&__grad2_1_2_beta1,bytes);
		 cudaMalloc((void **)&__grad2_2_2_beta1,bytes);
		 cudaMalloc((void **)&__grad2_0_0_beta2,bytes);
		 cudaMalloc((void **)&__grad2_0_1_beta2,bytes);
		 cudaMalloc((void **)&__grad2_0_2_beta2,bytes);
		 cudaMalloc((void **)&__grad2_1_1_beta2,bytes);
		 cudaMalloc((void **)&__grad2_1_2_beta2,bytes);
		 cudaMalloc((void **)&__grad2_2_2_beta2,bytes);
		 cudaMalloc((void **)&__agrad_0_gt0,bytes);
		 cudaMalloc((void **)&__agrad_1_gt0,bytes);
		 cudaMalloc((void **)&__agrad_2_gt0,bytes);
		 cudaMalloc((void **)&__agrad_0_gt1,bytes);
		 cudaMalloc((void **)&__agrad_1_gt1,bytes);
		 cudaMalloc((void **)&__agrad_2_gt1,bytes);
		 cudaMalloc((void **)&__agrad_0_gt2,bytes);
		 cudaMalloc((void **)&__agrad_1_gt2,bytes);
		 cudaMalloc((void **)&__agrad_2_gt2,bytes);
		 cudaMalloc((void **)&__agrad_0_gt3,bytes);
		 cudaMalloc((void **)&__agrad_1_gt3,bytes);
		 cudaMalloc((void **)&__agrad_2_gt3,bytes);
		 cudaMalloc((void **)&__agrad_0_gt4,bytes);
		 cudaMalloc((void **)&__agrad_1_gt4,bytes);
		 cudaMalloc((void **)&__agrad_2_gt4,bytes);
		 cudaMalloc((void **)&__agrad_0_gt5,bytes);
		 cudaMalloc((void **)&__agrad_1_gt5,bytes);
		 cudaMalloc((void **)&__agrad_2_gt5,bytes);
		 cudaMalloc((void **)&__agrad_0_At0,bytes);
		 cudaMalloc((void **)&__agrad_1_At0,bytes);
		 cudaMalloc((void **)&__agrad_2_At0,bytes);
		 cudaMalloc((void **)&__agrad_0_At1,bytes);
		 cudaMalloc((void **)&__agrad_1_At1,bytes);
		 cudaMalloc((void **)&__agrad_2_At1,bytes);
		 cudaMalloc((void **)&__agrad_0_At2,bytes);
		 cudaMalloc((void **)&__agrad_1_At2,bytes);
		 cudaMalloc((void **)&__agrad_2_At2,bytes);
		 cudaMalloc((void **)&__agrad_0_At3,bytes);
		 cudaMalloc((void **)&__agrad_1_At3,bytes);
		 cudaMalloc((void **)&__agrad_2_At3,bytes);
		 cudaMalloc((void **)&__agrad_0_At4,bytes);
		 cudaMalloc((void **)&__agrad_1_At4,bytes);
		 cudaMalloc((void **)&__agrad_2_At4,bytes);
		 cudaMalloc((void **)&__agrad_0_At5,bytes);
		 cudaMalloc((void **)&__agrad_1_At5,bytes);
		 cudaMalloc((void **)&__agrad_2_At5,bytes);
		 cudaMalloc((void **)&__agrad_0_alpha,bytes);
		 cudaMalloc((void **)&__agrad_1_alpha,bytes);
		 cudaMalloc((void **)&__agrad_2_alpha,bytes);
		 cudaMalloc((void **)&__agrad_0_beta0,bytes);
		 cudaMalloc((void **)&__agrad_1_beta0,bytes);
		 cudaMalloc((void **)&__agrad_2_beta0,bytes);
		 cudaMalloc((void **)&__agrad_0_beta1,bytes);
		 cudaMalloc((void **)&__agrad_1_beta1,bytes);
		 cudaMalloc((void **)&__agrad_2_beta1,bytes);
		 cudaMalloc((void **)&__agrad_0_beta2,bytes);
		 cudaMalloc((void **)&__agrad_1_beta2,bytes);
		 cudaMalloc((void **)&__agrad_2_beta2,bytes);
		 cudaMalloc((void **)&__agrad_0_chi,bytes);
		 cudaMalloc((void **)&__agrad_1_chi,bytes);
		 cudaMalloc((void **)&__agrad_2_chi,bytes);
		 cudaMalloc((void **)&__agrad_0_Gt0,bytes);
		 cudaMalloc((void **)&__agrad_1_Gt0,bytes);
		 cudaMalloc((void **)&__agrad_2_Gt0,bytes);
		 cudaMalloc((void **)&__agrad_0_Gt1,bytes);
		 cudaMalloc((void **)&__agrad_1_Gt1,bytes);
		 cudaMalloc((void **)&__agrad_2_Gt1,bytes);
		 cudaMalloc((void **)&__agrad_0_Gt2,bytes);
		 cudaMalloc((void **)&__agrad_1_Gt2,bytes);
		 cudaMalloc((void **)&__agrad_2_Gt2,bytes);
		 cudaMalloc((void **)&__agrad_0_K,bytes);
		 cudaMalloc((void **)&__agrad_1_K,bytes);
		 cudaMalloc((void **)&__agrad_2_K,bytes);
		 cudaMalloc((void **)&__agrad_0_B0,bytes);
		 cudaMalloc((void **)&__agrad_1_B0,bytes);
		 cudaMalloc((void **)&__agrad_2_B0,bytes);
		 cudaMalloc((void **)&__agrad_0_B1,bytes);
		 cudaMalloc((void **)&__agrad_1_B1,bytes);
		 cudaMalloc((void **)&__agrad_2_B1,bytes);
		 cudaMalloc((void **)&__agrad_0_B2,bytes);
		 cudaMalloc((void **)&__agrad_1_B2,bytes);
		 cudaMalloc((void **)&__agrad_2_B2,bytes);
		 cudaMalloc((void **)&__kograd_0_alpha,bytes);
		 cudaMalloc((void **)&__kograd_1_alpha,bytes);
		 cudaMalloc((void **)&__kograd_2_alpha,bytes);


} 


	/**@brief memory deallocation for deriv variables */
	void cuda::MemoryDerivs::deallocateDerivMemory(){ 
		 cudaFree((void **)&__grad_0_alpha);
		 cudaFree((void **)&__grad_1_alpha);
		 cudaFree((void **)&__grad_2_alpha);
		 cudaFree((void **)&__grad2_0_0_gt0);
		 cudaFree((void **)&__grad2_0_1_gt0);
		 cudaFree((void **)&__grad2_0_2_gt0);
		 cudaFree((void **)&__grad2_1_1_gt0);
		 cudaFree((void **)&__grad2_1_2_gt0);
		 cudaFree((void **)&__grad2_2_2_gt0);
		 cudaFree((void **)&__grad2_0_0_gt1);
		 cudaFree((void **)&__grad2_0_1_gt1);
		 cudaFree((void **)&__grad2_0_2_gt1);
		 cudaFree((void **)&__grad2_1_1_gt1);
		 cudaFree((void **)&__grad2_1_2_gt1);
		 cudaFree((void **)&__grad2_2_2_gt1);
		 cudaFree((void **)&__grad2_0_0_gt2);
		 cudaFree((void **)&__grad2_0_1_gt2);
		 cudaFree((void **)&__grad2_0_2_gt2);
		 cudaFree((void **)&__grad2_1_1_gt2);
		 cudaFree((void **)&__grad2_1_2_gt2);
		 cudaFree((void **)&__grad2_2_2_gt2);
		 cudaFree((void **)&__grad2_0_0_gt3);
		 cudaFree((void **)&__grad2_0_1_gt3);
		 cudaFree((void **)&__grad2_0_2_gt3);
		 cudaFree((void **)&__grad2_1_1_gt3);
		 cudaFree((void **)&__grad2_1_2_gt3);
		 cudaFree((void **)&__grad2_2_2_gt3);
		 cudaFree((void **)&__grad2_0_0_gt4);
		 cudaFree((void **)&__grad2_0_1_gt4);
		 cudaFree((void **)&__grad2_0_2_gt4);
		 cudaFree((void **)&__grad2_1_1_gt4);
		 cudaFree((void **)&__grad2_1_2_gt4);
		 cudaFree((void **)&__grad2_2_2_gt4);
		 cudaFree((void **)&__grad2_0_0_gt5);
		 cudaFree((void **)&__grad2_0_1_gt5);
		 cudaFree((void **)&__grad2_0_2_gt5);
		 cudaFree((void **)&__grad2_1_1_gt5);
		 cudaFree((void **)&__grad2_1_2_gt5);
		 cudaFree((void **)&__grad2_2_2_gt5);
		 cudaFree((void **)&__grad2_0_0_chi);
		 cudaFree((void **)&__grad2_0_1_chi);
		 cudaFree((void **)&__grad2_0_2_chi);
		 cudaFree((void **)&__grad2_1_1_chi);
		 cudaFree((void **)&__grad2_1_2_chi);
		 cudaFree((void **)&__grad2_2_2_chi);
		 cudaFree((void **)&__grad2_0_0_alpha);
		 cudaFree((void **)&__grad2_0_1_alpha);
		 cudaFree((void **)&__grad2_0_2_alpha);
		 cudaFree((void **)&__grad2_1_1_alpha);
		 cudaFree((void **)&__grad2_1_2_alpha);
		 cudaFree((void **)&__grad2_2_2_alpha);
		 cudaFree((void **)&__grad2_0_0_beta0);
		 cudaFree((void **)&__grad2_0_1_beta0);
		 cudaFree((void **)&__grad2_0_2_beta0);
		 cudaFree((void **)&__grad2_1_1_beta0);
		 cudaFree((void **)&__grad2_1_2_beta0);
		 cudaFree((void **)&__grad2_2_2_beta0);
		 cudaFree((void **)&__grad2_0_0_beta1);
		 cudaFree((void **)&__grad2_0_1_beta1);
		 cudaFree((void **)&__grad2_0_2_beta1);
		 cudaFree((void **)&__grad2_1_1_beta1);
		 cudaFree((void **)&__grad2_1_2_beta1);
		 cudaFree((void **)&__grad2_2_2_beta1);
		 cudaFree((void **)&__grad2_0_0_beta2);
		 cudaFree((void **)&__grad2_0_1_beta2);
		 cudaFree((void **)&__grad2_0_2_beta2);
		 cudaFree((void **)&__grad2_1_1_beta2);
		 cudaFree((void **)&__grad2_1_2_beta2);
		 cudaFree((void **)&__grad2_2_2_beta2);
		 cudaFree((void **)&__agrad_0_gt0);
		 cudaFree((void **)&__agrad_1_gt0);
		 cudaFree((void **)&__agrad_2_gt0);
		 cudaFree((void **)&__agrad_0_gt1);
		 cudaFree((void **)&__agrad_1_gt1);
		 cudaFree((void **)&__agrad_2_gt1);
		 cudaFree((void **)&__agrad_0_gt2);
		 cudaFree((void **)&__agrad_1_gt2);
		 cudaFree((void **)&__agrad_2_gt2);
		 cudaFree((void **)&__agrad_0_gt3);
		 cudaFree((void **)&__agrad_1_gt3);
		 cudaFree((void **)&__agrad_2_gt3);
		 cudaFree((void **)&__agrad_0_gt4);
		 cudaFree((void **)&__agrad_1_gt4);
		 cudaFree((void **)&__agrad_2_gt4);
		 cudaFree((void **)&__agrad_0_gt5);
		 cudaFree((void **)&__agrad_1_gt5);
		 cudaFree((void **)&__agrad_2_gt5);
		 cudaFree((void **)&__agrad_0_At0);
		 cudaFree((void **)&__agrad_1_At0);
		 cudaFree((void **)&__agrad_2_At0);
		 cudaFree((void **)&__agrad_0_At1);
		 cudaFree((void **)&__agrad_1_At1);
		 cudaFree((void **)&__agrad_2_At1);
		 cudaFree((void **)&__agrad_0_At2);
		 cudaFree((void **)&__agrad_1_At2);
		 cudaFree((void **)&__agrad_2_At2);
		 cudaFree((void **)&__agrad_0_At3);
		 cudaFree((void **)&__agrad_1_At3);
		 cudaFree((void **)&__agrad_2_At3);
		 cudaFree((void **)&__agrad_0_At4);
		 cudaFree((void **)&__agrad_1_At4);
		 cudaFree((void **)&__agrad_2_At4);
		 cudaFree((void **)&__agrad_0_At5);
		 cudaFree((void **)&__agrad_1_At5);
		 cudaFree((void **)&__agrad_2_At5);
		 cudaFree((void **)&__agrad_0_alpha);
		 cudaFree((void **)&__agrad_1_alpha);
		 cudaFree((void **)&__agrad_2_alpha);
		 cudaFree((void **)&__agrad_0_beta0);
		 cudaFree((void **)&__agrad_1_beta0);
		 cudaFree((void **)&__agrad_2_beta0);
		 cudaFree((void **)&__agrad_0_beta1);
		 cudaFree((void **)&__agrad_1_beta1);
		 cudaFree((void **)&__agrad_2_beta1);
		 cudaFree((void **)&__agrad_0_beta2);
		 cudaFree((void **)&__agrad_1_beta2);
		 cudaFree((void **)&__agrad_2_beta2);
		 cudaFree((void **)&__agrad_0_chi);
		 cudaFree((void **)&__agrad_1_chi);
		 cudaFree((void **)&__agrad_2_chi);
		 cudaFree((void **)&__agrad_0_Gt0);
		 cudaFree((void **)&__agrad_1_Gt0);
		 cudaFree((void **)&__agrad_2_Gt0);
		 cudaFree((void **)&__agrad_0_Gt1);
		 cudaFree((void **)&__agrad_1_Gt1);
		 cudaFree((void **)&__agrad_2_Gt1);
		 cudaFree((void **)&__agrad_0_Gt2);
		 cudaFree((void **)&__agrad_1_Gt2);
		 cudaFree((void **)&__agrad_2_Gt2);
		 cudaFree((void **)&__agrad_0_K);
		 cudaFree((void **)&__agrad_1_K);
		 cudaFree((void **)&__agrad_2_K);
		 cudaFree((void **)&__agrad_0_B0);
		 cudaFree((void **)&__agrad_1_B0);
		 cudaFree((void **)&__agrad_2_B0);
		 cudaFree((void **)&__agrad_0_B1);
		 cudaFree((void **)&__agrad_1_B1);
		 cudaFree((void **)&__agrad_2_B1);
		 cudaFree((void **)&__agrad_0_B2);
		 cudaFree((void **)&__agrad_1_B2);
		 cudaFree((void **)&__agrad_2_B2);
		 cudaFree((void **)&__kograd_0_alpha);
		 cudaFree((void **)&__kograd_1_alpha);
		 cudaFree((void **)&__kograd_2_alpha);


} 


}// end of namespace cuda
