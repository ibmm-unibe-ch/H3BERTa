#!/bin/bash
BEST_MODEL=$(pwd)

## rain donor 3 unique cdrh3
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/SOTA:RAIN/donor3(bnabs)/donor3_repertoire_uniqueCDRH3_id_seq_label.csv" --model_path $BEST_MODEL

## rain donor 3 with duplicates 
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/SOTA:RAIN/donor3(bnabs)/donor3_repertoire_cdrh3_id_seq_label.csv" --model_path $BEST_MODEL

mkdir outputs/donor3_repertoire_uniqueCDRH3
mv donor3_repertoire_uniqueCDRH3* outputs/donor3_repertoire_uniqueCDRH3

mkdir outputs/donor3_repertoire_cdrh3
mv donor3_repertoire_cdrh3* outputs/donor3_repertoire_cdrh3


### RAIN DONOR3 UNIQUE CDRH3
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/donor3_repertoire_uniqueCDRH3/*.npz --run_dim_reduction

### RAIN DONOR3 ENTIRE REPERTOIRE 
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/donor3_repertoire_cdrh3/*.npz --run_dim_reduction


## unlabel cincinnati
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/all_repertoires/bnabs/bnabs_repertoire_withcdrh3duplicates_703010564.txt" --model_path $BEST_MODEL
