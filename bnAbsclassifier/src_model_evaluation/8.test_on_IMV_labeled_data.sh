#!/bin/bash
BEST_MODEL=$(pwd)
### imv data only
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/V1_LINCLUST/TRAINING_DATASET/NOIMV/IMV_only_BRONON.csv" --model_path $BEST_MODEL

mkdir outputs/IMV_only_BRONON
mv IMV_only_BRONON* /outputs/IMV_only_BRONON
