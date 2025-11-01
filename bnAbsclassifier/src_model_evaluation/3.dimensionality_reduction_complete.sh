#!/bin/bash
mkdir dimensionality_reduction_complete

### IMV LAB
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction_complete.py --embeddings ./outputs/3_22_24_patient_repertoire_complete_info_IMV_lab/*.npz --run_dim_reduction

### IMV LAB WITH DUPLICATES
#python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction_complete.py  --run_dim_reduction --embeddings ./outputs/3_22_24_with_duplicates/*.npz


