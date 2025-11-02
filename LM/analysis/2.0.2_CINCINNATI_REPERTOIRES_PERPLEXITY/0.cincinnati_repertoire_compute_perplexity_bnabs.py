from transformers import AutoTokenizer, AutoModelForMaskedLM
import pandas as pd
import sys
sys.path.append("./src/")
from perplexity import calculate_pseudo_perplexity
from tqdm import tqdm
import os

BEST_MODEL="/ibmm_data/rodelc/DALM/LM/HEAVY/CDRH3/HEALTHY/P3-pipelines/model/SUB-PIPELINE1:IgG_IgA_Bsources/config3.json_lr5e-5_bs1024/BEST_MODEL/epoch_113/hf"  
# Modello e tokenizer
tokenizer = AutoTokenizer.from_pretrained(BEST_MODEL)
model = AutoModelForMaskedLM.from_pretrained(BEST_MODEL)


# Percorso della directory con i file
directory = "/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/all_repertoires/bnabs"
out_directory = "./cincinnati_repertoires_check/"

# Assicurati che la cartella di output esista
os.makedirs(out_directory, exist_ok=True)

# Lista di tutti i file da processare
all_files = [f for f in os.listdir(directory) if f.endswith(".txt") or f.endswith(".csv")]

# File per log degli errori
error_log_file = "error_log.txt"
failed_files = []

# Barra di progresso per i file
for filename in tqdm(all_files, desc="Processing files", unit="file"):
    file_path = os.path.join(directory, filename)
    
    try:
        # Carica il file
        df = pd.read_csv(file_path, header=None)
        df.columns = ['id', 'sequence', 'label','v_identity','d_identity','j_identity','v_family', 'd_family','j_family','c_family']
        df = df.dropna(subset=['sequence'])

        # Calcola la perplessità
        tqdm.pandas()
        df["perplexity"] = df["sequence"].progress_apply(lambda seq: calculate_pseudo_perplexity(seq, model, tokenizer))

        # Conta le occorrenze di ogni sequenza
        df["frequency"] = df.groupby("sequence")["sequence"].transform("count")

        # Salva il file con un nuovo nome
        output_filename = filename.replace(".txt", "_perplexity.csv").replace(".csv", "_perplexity.csv")
        output_path = os.path.join(out_directory, output_filename)
        df.to_csv(output_path, index=False)

        print(f"Processed: {filename} -> {output_filename}")

    except Exception as e:
        print(f"Errore con il file {filename}: {e}")
        failed_files.append(filename)

# Salva il log degli errori
if failed_files:
    with open(error_log_file, "a") as f:
        for file in failed_files:
            f.write(file + "\n")
    print(f"File con errori salvati in: {error_log_file}")


###############################
#hhiv_repertoire_withcdrh3duplicates_703010619iv_repertoire_withcdrh3duplicates_703010619 ll-

##################################

# Data: 
#df = pd.read_csv('/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/healthy_repertoire_withcdrh3duplicates_704010146.txt',header=None)
#df = pd.read_csv('/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/hiv_repertoire_withcdrh3duplicates_700010333.txt',header=None)
#df = pd.read_csv('/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/UNLABEL/repertoires/hiv_with_NEU_repertoire_withcdrh3duplicates_704010453.txt',header=None)
#df = pd.read_csv('/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/data/SOTA:RAIN/donor2(nobnabs)/donor2_repertoire_cdrh3_id_seq_label.csv',header=None)
#df.columns = ['id','sequence','label'] #'label_lab'
#df = df.dropna(subset=['sequence'])

# Calcola perplexity per ogni sequenza nel dataset
# Aggiungi il supporto per la visualizzazione del progresso
#tqdm.pandas()
#df["perplexity"] = df["sequence"].progress_apply(lambda seq: calculate_pseudo_perplexity(seq, model, tokenizer))

# Conta le occorrenze di ogni sequenza
#df["frequency"] = df.groupby("sequence")["sequence"].transform("count")
#df.to_csv('healthy_repertoire_withcdrh3duplicates_704010146_perplexity.csv', index=False)  
#df.to_csv('hiv_repertoire_withcdrh3duplicates_700010333_perplexity.csv', index=False) 
#df.to_csv('hiv_with_NEU_repertoire_withcdrh3duplicates_704010453_perplexity.csv', index=False) 
#df.to_csv('RAIN_donor2_repertoire_cdrh3_nobnabs_perplexity.csv', index=False) 