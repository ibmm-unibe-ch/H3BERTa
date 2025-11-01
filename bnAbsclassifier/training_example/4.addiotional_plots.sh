#!/bin/bash


### test set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/label_test/label_test_shuffled_BRO_NON_test_out_df.csv --save_dir ./additional_plots

## train set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/label_train/label_train_shuffled_BRO_NON_test_out_df.csv --save_dir ./additional_plots

## val set
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/label_val/label_val_shuffled_BRO_NON_test_out_df.csv --save_dir ./additional_plots

## 3_22_24_IMV_LAB
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/3_22_24_IMV_LAB/3_22_24_patient_repertoire_IMV_lab_test_out_df.csv --save_dir ./additional_plots

## 3_22_24_IMV_LAB WITH DUPLICATES
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/3_22_24_IMV_LAB/patient_repertoire_3_22_24_withduplicates_IMV_lab_test_out_df.csv --save_dir ./additional_plots
