import os
from evaluate_mlm import main

MODEL_PATH = "/ibmm_data/rodelc/DALM/LM/HEAVY/CDRH3/HEALTHY/P3-pipelines/model/SUB-PIPELINE1:IgG_IgA_Bsources/config3.json_lr5e-5_bs1024/BEST_MODEL/epoch_113/hf"  


MODEL_NAME ='H3BERTA_HEALTHY_TAILS'
CSV_FILE = './tails_analysis/healthy_with_tail_labels.csv'
EMBEDDING_FILE = f"./tails_analysis/{MODEL_NAME}_embeddings.pkl"
PLOT_TITLE = MODEL_NAME+' PCA embeddings'
HUE_CLASS = 'tail'
REDUCTION_OUTPUT_PATH = './tails_analysis'
main(MODEL_NAME, MODEL_PATH, CSV_FILE, EMBEDDING_FILE, PLOT_TITLE, HUE_CLASS, REDUCTION_OUTPUT_PATH, umap=True, pca=True)

