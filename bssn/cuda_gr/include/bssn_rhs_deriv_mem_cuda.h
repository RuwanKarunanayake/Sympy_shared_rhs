// generated by bssnUtils.py code for derivative allocations and deallocations
//date: 2018-09-06 14:54:50
#ifndef BSSN_RHS_DERIV_ALLOC 
#define BSSN_RHS_DERIV_ALLOC

#include <iostream>
#include "cuda_runtime.h"

namespace cuda {
	struct MemoryDerivs{

	 unsigned int __maxBlkSz;
	 double* __grad_0_alpha;
	 double* __grad_1_alpha;
	 double* __grad_2_alpha;
	 double* __grad2_0_0_gt0;
	 double* __grad2_0_1_gt0;
	 double* __grad2_0_2_gt0;
	 double* __grad2_1_1_gt0;
	 double* __grad2_1_2_gt0;
	 double* __grad2_2_2_gt0;
	 double* __grad2_0_0_gt1;
	 double* __grad2_0_1_gt1;
	 double* __grad2_0_2_gt1;
	 double* __grad2_1_1_gt1;
	 double* __grad2_1_2_gt1;
	 double* __grad2_2_2_gt1;
	 double* __grad2_0_0_gt2;
	 double* __grad2_0_1_gt2;
	 double* __grad2_0_2_gt2;
	 double* __grad2_1_1_gt2;
	 double* __grad2_1_2_gt2;
	 double* __grad2_2_2_gt2;
	 double* __grad2_0_0_gt3;
	 double* __grad2_0_1_gt3;
	 double* __grad2_0_2_gt3;
	 double* __grad2_1_1_gt3;
	 double* __grad2_1_2_gt3;
	 double* __grad2_2_2_gt3;
	 double* __grad2_0_0_gt4;
	 double* __grad2_0_1_gt4;
	 double* __grad2_0_2_gt4;
	 double* __grad2_1_1_gt4;
	 double* __grad2_1_2_gt4;
	 double* __grad2_2_2_gt4;
	 double* __grad2_0_0_gt5;
	 double* __grad2_0_1_gt5;
	 double* __grad2_0_2_gt5;
	 double* __grad2_1_1_gt5;
	 double* __grad2_1_2_gt5;
	 double* __grad2_2_2_gt5;
	 double* __grad2_0_0_chi;
	 double* __grad2_0_1_chi;
	 double* __grad2_0_2_chi;
	 double* __grad2_1_1_chi;
	 double* __grad2_1_2_chi;
	 double* __grad2_2_2_chi;
	 double* __grad2_0_0_alpha;
	 double* __grad2_0_1_alpha;
	 double* __grad2_0_2_alpha;
	 double* __grad2_1_1_alpha;
	 double* __grad2_1_2_alpha;
	 double* __grad2_2_2_alpha;
	 double* __grad2_0_0_beta0;
	 double* __grad2_0_1_beta0;
	 double* __grad2_0_2_beta0;
	 double* __grad2_1_1_beta0;
	 double* __grad2_1_2_beta0;
	 double* __grad2_2_2_beta0;
	 double* __grad2_0_0_beta1;
	 double* __grad2_0_1_beta1;
	 double* __grad2_0_2_beta1;
	 double* __grad2_1_1_beta1;
	 double* __grad2_1_2_beta1;
	 double* __grad2_2_2_beta1;
	 double* __grad2_0_0_beta2;
	 double* __grad2_0_1_beta2;
	 double* __grad2_0_2_beta2;
	 double* __grad2_1_1_beta2;
	 double* __grad2_1_2_beta2;
	 double* __grad2_2_2_beta2;
	 double* __agrad_0_gt0;
	 double* __agrad_1_gt0;
	 double* __agrad_2_gt0;
	 double* __agrad_0_gt1;
	 double* __agrad_1_gt1;
	 double* __agrad_2_gt1;
	 double* __agrad_0_gt2;
	 double* __agrad_1_gt2;
	 double* __agrad_2_gt2;
	 double* __agrad_0_gt3;
	 double* __agrad_1_gt3;
	 double* __agrad_2_gt3;
	 double* __agrad_0_gt4;
	 double* __agrad_1_gt4;
	 double* __agrad_2_gt4;
	 double* __agrad_0_gt5;
	 double* __agrad_1_gt5;
	 double* __agrad_2_gt5;
	 double* __agrad_0_At0;
	 double* __agrad_1_At0;
	 double* __agrad_2_At0;
	 double* __agrad_0_At1;
	 double* __agrad_1_At1;
	 double* __agrad_2_At1;
	 double* __agrad_0_At2;
	 double* __agrad_1_At2;
	 double* __agrad_2_At2;
	 double* __agrad_0_At3;
	 double* __agrad_1_At3;
	 double* __agrad_2_At3;
	 double* __agrad_0_At4;
	 double* __agrad_1_At4;
	 double* __agrad_2_At4;
	 double* __agrad_0_At5;
	 double* __agrad_1_At5;
	 double* __agrad_2_At5;
	 double* __agrad_0_alpha;
	 double* __agrad_1_alpha;
	 double* __agrad_2_alpha;
	 double* __agrad_0_beta0;
	 double* __agrad_1_beta0;
	 double* __agrad_2_beta0;
	 double* __agrad_0_beta1;
	 double* __agrad_1_beta1;
	 double* __agrad_2_beta1;
	 double* __agrad_0_beta2;
	 double* __agrad_1_beta2;
	 double* __agrad_2_beta2;
	 double* __agrad_0_chi;
	 double* __agrad_1_chi;
	 double* __agrad_2_chi;
	 double* __agrad_0_Gt0;
	 double* __agrad_1_Gt0;
	 double* __agrad_2_Gt0;
	 double* __agrad_0_Gt1;
	 double* __agrad_1_Gt1;
	 double* __agrad_2_Gt1;
	 double* __agrad_0_Gt2;
	 double* __agrad_1_Gt2;
	 double* __agrad_2_Gt2;
	 double* __agrad_0_K;
	 double* __agrad_1_K;
	 double* __agrad_2_K;
	 double* __agrad_0_B0;
	 double* __agrad_1_B0;
	 double* __agrad_2_B0;
	 double* __agrad_0_B1;
	 double* __agrad_1_B1;
	 double* __agrad_2_B1;
	 double* __agrad_0_B2;
	 double* __agrad_1_B2;
	 double* __agrad_2_B2;
	 double* __kograd_0_alpha;
	 double* __kograd_1_alpha;
	 double* __kograd_2_alpha;


	/**@brief memory allocation for deriv variables */
	void allocateDerivMemory(unsigned int maxBlkSz); 


	/**@brief memory deallocation for deriv variables */
	void deallocateDerivMemory(); 


	};

}// end of namespace cuda

#endif
