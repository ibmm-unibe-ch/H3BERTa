import os
from evaluate_mlm import main
import pandas as pd

MODEL_PATH = "/ibmm_data/rodelc/DALM/LM/HEAVY/CDRH3/HEALTHY/P3-pipelines/model/SUB-PIPELINE1:IgG_IgA_Bsources/config3.json_lr5e-5_bs1024/BEST_MODEL/epoch_113/hf"

# Percorso al file CSV specifico
DATA_PATH = "../../50knaive_50kmemory_oas_paired_randomly_selected.csv"

# (Opzionale) Colonne attese, se vuoi forzare qualcosa
columns = [
    "sequence_heavy",
    "locus_heavy",
    "v_call_heavy",
    "sequence_alignment_heavy",
    "sequence_alignment_aa_heavy",
    "germline_alignment_aa_heavy",
    "cdr3_aa_heavy",
    "sequence_light",
    "locus_light",
    "v_call_light",
    "sequence_alignment_light",
    "sequence_alignment_aa_light",
    "germline_alignment_aa_light",
    "cdr3_aa_light",
    "sequence_alignment_heavy_sep_light",
    "BType",
    "Disease",
    "Species",
]

# Output directory
REDUCTION_OUTPUT_PATH = "./out_embeddings/"

# Legge direttamente il CSV specificato
df = pd.read_csv(DATA_PATH, header=0)
print(df.head(2))

# Rinomina la colonna
df.rename(columns={"cdr3_aa_light": "sequence"}, inplace=True)

# Filtra per tenere solo sequenze con una sola riga coerente
df = (
    df.groupby("sequence", as_index=False)
      .filter(lambda g: len(g.drop_duplicates()) == 1)
      .drop_duplicates(subset="sequence")
)
print(df['sequence'])
# Salva un CSV temporaneo da passare alla funzione main
tmp_csv_path = "/tmp/tmp_data.csv"
df.to_csv(tmp_csv_path, index=False)

# Costruisce il nome del modello a partire dal nome del file
filename = os.path.basename(DATA_PATH)  # es. 50knaive_50kmemory_oas_paired_randomly_selected.csv
model_name = "H3BERTA_" + filename.replace(".csv", "").upper()

embedding_file = f"./{model_name}_embeddings.pkl"
plot_title = model_name + " PCA embeddings"
hue_class = "v_call_light"

print(f"Running model: {model_name}")

main(
    model_name,
    MODEL_PATH,
    tmp_csv_path,
    embedding_file,
    plot_title,
    hue_class,
    REDUCTION_OUTPUT_PATH,
    umap=True,
    pca=True,
)
