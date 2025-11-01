#!/bin/bash

BEST_MODEL=$(pwd)

################################# TEST SET 2 LABELS #################################################

### val set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/HAMMING_DISTANCE_CLUSTERING_approach/2.TRAINING_DATASET/v2_per_category/binary_50pident_val.txt" --model_path $BEST_MODEL


## test set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/HAMMING_DISTANCE_CLUSTERING_approach/2.TRAINING_DATASET/v2_per_category/binary_50pident_test.txt" --model_path $BEST_MODEL


## train set just to have embeddings
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/HAMMING_DISTANCE_CLUSTERING_approach/2.TRAINING_DATASET/v2_per_category/binary_50pident_train.txt" --model_path $BEST_MODEL


# imv repertoire 
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/3_22_24_patient_repertoire_IMV_lab.txt" --model_path $BEST_MODEL

# imv repertoire with duplicates
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/patient_repertoire_3_22_24_withduplicates_IMV_lab.txt" --model_path $BEST_MODEL

## repertoire testing
/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/repertoire_testing_embeddings_output.sh $BEST_MODEL
