#!/bin/bash
BEST_MODEL=$(pwd)

for repertoire in /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/LABEL/0_IMV/HIV_REPERTOIRE/patients_repertoires/* ; do
    file=$(basename "$repertoire") 
    file="${file%.*}"
    
    echo "Repertoire: $file"
    python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/test_embeddings_extraction.py --test_file "$repertoire" --model_path "$BEST_MODEL"
    
    mkdir outputs/"$file"
    mv "$file"* outputs/"$file"
    
    python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/dimensionality_reduction.py --embeddings ./outputs/"$file"/*.npz  --run_dim_reduction
    
    python /ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/BEST_RESULTS/H3BERTA:HEALTHY:CDRH3:P3:JUNE2024/src/classification_score_plot.py --test_out_df ./outputs/"$file"/*csv --save_dir ./additional_plots


done

