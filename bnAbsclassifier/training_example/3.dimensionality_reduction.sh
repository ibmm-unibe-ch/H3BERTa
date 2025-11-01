#!/bin/bash

## test set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/label_test/*.npz  --run_dim_reduction

## train set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/label_train/*.npz  --run_dim_reduction

##val set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/label_val/*.npz  --run_dim_reduction

### IMV LAB
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/3_22_24_IMV_LAB/*.npz --run_dim_reduction

### IMV LAB WITH DUPLICATES
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/3_22_24_with_duplicates/*.npz --run_dim_reduction
