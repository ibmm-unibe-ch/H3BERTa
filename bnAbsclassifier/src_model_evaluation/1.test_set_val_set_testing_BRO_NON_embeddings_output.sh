#!/bin/bash
BEST_MODEL=$(pwd)
mkdir additional_plots
### val set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/V1_LINCLUST/TRAINING_DATASET/NOIMV/label_val_shuffled_BRONON.txt" --model_path $BEST_MODEL

## test set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/V1_LINCLUST/TRAINING_DATASET/NOIMV/label_test_shuffled_BRONON.txt" --model_path $BEST_MODEL

## train set just to have embeddings
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/V1_LINCLUST/TRAINING_DATASET/NOIMV/label_train_shuffled_BRONON.txt" --model_path $BEST_MODEL

# imv repertoire 
#python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/3_22_24_patient_repertoire_IMV_lab.txt" --model_path $BEST_MODEL

# imv repertoire with duplicates
#python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/patient_repertoire_3_22_24_withduplicates_IMV_lab.txt" --model_path $BEST_MODEL

## repertoire testing
#/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/repertoire_testing_embeddings_output.sh $BEST_MODEL

## rain donor 3 unique cdrh3
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/SOTA:RAIN/donor3(bnabs)/donor3_repertoire_uniqueCDRH3_id_seq_label.csv" --model_path $BEST_MODEL

## rain donor 3 with duplicates 
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/SOTA:RAIN/donor3(bnabs)/donor3_repertoire_cdrh3_id_seq_label.csv" --model_path $BEST_MODEL

# imv repertoire no duplicates COMPLETE INFO
#python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/testing_embeddings_output.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/HIV_REPERTOIRE_COMPLETE_INFO/patients_repertoires/3_22_24_repertoire_noduplicates_complete_info.csv" --model_path $BEST_MODEL

# imv repertoire COMPLETE INFO + LAB LABELS
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/HIV_REPERTOIRE_COMPLETE_INFO/3_22_24_patient_repertoire_complete_info_IMV_lab.csv" --model_path $BEST_MODEL


### imv data only
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/V1_LINCLUST/TRAINING_DATASET/NOIMV/IMV_only_BRONON.csv" --model_path $BEST_MODEL

#healthy cincinnati
 python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/all_repertoires/healthy/healthy_repertoire_withcdrh3duplicates_700011206.txt" --model_path $BEST_MODEL

#bnabs cincinnati
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/all_repertoires/bnabs/bnabs_repertoire_withcdrh3duplicates_702010293.txt" --model_path $BEST_MODEL
