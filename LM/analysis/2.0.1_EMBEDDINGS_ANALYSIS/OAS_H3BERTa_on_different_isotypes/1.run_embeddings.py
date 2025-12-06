import os
from evaluate_mlm import main
import pandas as pd

MODEL_PATH = "/ibmm_data/rodelc/DALM/LM/HEAVY/CDRH3/HEALTHY/P3-pipelines/model/SUB-PIPELINE1:IgG_IgA_Bsources/config3.json_lr5e-5_bs1024/BEST_MODEL/epoch_113/hf"  

#Percorso alla cartella dei file .txt
TXT_DIR = '/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/all_repertoires/bnabs'

# Colonne da assegnare manualmente ai file .txt
columns = ['sequence_id', 'sequence', 'label', 'v_identity', 'd_identity', 'j_identity','v_family', 'd_family', 'j_family', 'c_family']

# Output directory
REDUCTION_OUTPUT_PATH = './out_bnabs/'

for filename in os.listdir(TXT_DIR):
    if filename.endswith('.txt'):
        filepath = os.path.join(TXT_DIR, filename)

        # Legge il file come CSV senza intestazione, ma con separatore ','
        df = pd.read_csv(filepath, header=None, names=columns)
        df = (
        df.groupby('sequence', as_index=False)                # raggruppa per sequenza
        .filter(lambda g: len(g.drop_duplicates()) == 1)    # scarta i gruppi "misti"
        .drop_duplicates(subset='sequence')                 # rimuove l'unico duplicato rimasto
    )

        # Ora puoi passare il dataframe direttamente, oppure salvarlo in memoria come CSV-like string
        # oppure modificare la funzione `main()` per accettare anche DataFrame in input
        # Qui lo salviamo temporaneamente in memoria come oggetto CSV per compatibilità
        tmp_csv_path = '/tmp/tmp_data.csv'
        df.to_csv(tmp_csv_path, index=False)

        model_name = 'H3BERTA_' + filename.replace('.txt', '').upper()
        embedding_file = f"./{model_name}_embeddings.pkl"
        plot_title = model_name + ' PCA embeddings'
        hue_class = 'v_family'

        print(f"Running model: {model_name}")

        main(model_name, MODEL_PATH, tmp_csv_path, embedding_file, plot_title, hue_class,
            REDUCTION_OUTPUT_PATH, umap=True, pca=True)