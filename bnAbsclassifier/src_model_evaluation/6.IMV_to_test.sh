#!/bin/bash
BEST_MODEL=$(pwd)


### euclidean_distance
repertoire='/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/IMV_validation/ROUND2/3_22_24_repertoire_FOR_PCA_euclidean_distance.csv'
file_name='3_22_24_FOR_IMV_euclidean_distance'
file=3_22_24_repertoire_FOR_PCA

python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "$repertoire" --model_path "$BEST_MODEL"
    
mkdir outputs/"$file_name"
mv "$file"* outputs/"$file_name"
    
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/"$file_name"/*.npz  --run_dim_reduction
    
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/"$file_name"/*csv --save_dir ./additional_plots

### 

repertoire='/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/IMV_validation/ROUND2/3_22_24_repertoire_FOR_PCA_equidistance_sampling.csv'
file_name='3_22_24_FOR_IMV_equidistance_sampling'
file=3_22_24_repertoire_FOR_PCA

python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "$repertoire" --model_path "$BEST_MODEL"
    
mkdir outputs/"$file_name"
mv "$file"* outputs/"$file_name"
    
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/"$file_name"/*.npz  --run_dim_reduction
    
python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/"$file_name"/*csv --save_dir ./additional_plots

