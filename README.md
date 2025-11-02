# H3BERTa: A CDR-H3 specific language model for antibody repertoire analysis
<p align="center">
  <img src="https://github.com/user-attachments/assets/c839ba2c-5958-4f2d-ad73-217839903dd1" width="500">
</p>


Zenodo record (DOI): `10.5281/zenodo.17505849`
The H3BERTa model weights are also available in a Hugging Face model [repository]([url](https://huggingface.co/Chrode/H3BERTa)).


This repository contains the code, pretrained models, and datasets used in the study:

> **Chiara Rodella & Thomas Lemmin**  
> *H3BERTa: A CDR-H3 specific language model for antibody repertoire analysis*  
> Institute of Biochemistry and Molecular Medicine, University of Bern (Switzerland)


This repository contains the code, configuration files, datasets, and analyses associated with the H3BERTa paper.
Large artifacts (datasets, trained weights, etc.) are stored on Zenodo and mirrored using the same directory structure as in this GitHub repo.

---

## Overview
```
H3BERTa/
├─ LM/               # H3BERTa language model training, data and analysis
├─ bnAbsclassifier/  # GAN-BERTa and SVM classifiers training and data for HIV-1 broadly neutralizing antibodies (bnAbs)
└─ README.md         # Project description
```

**Model ID:** `Chrode/H3BERTa`  
**Architecture:** RoBERTa-base (encoder-only, Masked Language Model)  
**Sequence type:** Heavy chain CDR-H3 regions  
**Training:** Pretrained on >17M curated CDR-H3 sequences from healthy donor repertoires (OAS, IgG/IgA sources)    
**Max sequence length:** 100 amino acids  
**Vocabulary:** 25 tokens (20 standard amino acids + special tokens)  
**Mask token:** `[MASK]`

---

## Model Overview

H3BERTa is a transformer-based language model trained specifically on the **Complementarity-Determining Region 3 of the heavy chain (CDR-H3)**, the most diverse and functionally critical region of antibodies.  
It captures the statistical regularities and biophysical constraints underlying natural antibody repertoires, enabling **embedding extraction**, **variant scoring**, and **context-aware mutation predictions**.

---

## Intended Use

- Embedding extraction for CDR-H3 repertoire analysis  
- Mutation impact scoring (pseudo-likelihood estimation)  
- Downstream fine-tuning (e.g., bnabs identification)  

---

## How to Use

**Input format**: CDR-H3 sequences must be provided as plain amino acid strings (e.g., "ARDRSTGGYFDY") without the initial “C” or terminal “W” residues, and without whitespace or separators between amino acids.

```python
from transformers import AutoTokenizer, AutoModel

model_id = "Chrode/H3BERTa"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModel.from_pretrained(model_id)
```

### Example #1: Embeddings extraction

Extract per-sequence embeddings useful for clustering, similarity search, or downstream ML models.
```python
from transformers import pipeline
import torch, numpy as np

feat = pipeline(
    task="feature-extraction",
    model="Chrode/H3BERTa",
    tokenizer="Chrode/H3BERTa",
    device=0 if torch.cuda.is_available() else -1
)

seqs = [
    "ARMGAAREWDFQY",
    "ARDGLGEVAPDYRYGIDV"
]

with torch.no_grad():
    outs = feat(seqs)

# Mean pooling across tokens → per-sequence embedding
embs = [np.array(o).mean(axis=0) for o in outs]
print(len(embs), embs[0].shape)
```

### Example #2: Masked-Language Modeling (Mutation Scoring)

Predict likely amino acids for masked positions or evaluate single-site mutations.

```python
from transformers import pipeline, AutoTokenizer

model_id = "Chrode/H3BERTa"
tok = AutoTokenizer.from_pretrained(model_id)

mlm = pipeline(
    task="fill-mask",
    model=model_id,
    tokenizer=tok,
    device=0
)

# Example: predict missing residue
seq = "CARDRS[MASK]GGYFDYW".replace("[MASK]", tok.mask_token)
preds = mlm(seq, top_k=10)

for p in preds:
    print(p["token_str"], round(p["score"], 4))

# Score a specific point mutation
AMINO = list("ACDEFGHIKLMNPQRSTVWY")

def score_point_mutation(seq, idx, mutant_aa):
    masked = seq[:idx] + tok.mask_token + seq[idx+1:]
    preds = mlm(masked, top_k=len(AMINO))
    for p in preds:
        if p["token_str"] == mutant_aa:
            return p["score"]
    return 0.0

wt = "ARDRSTGGYFDY"
print("R→A @ pos 3:", score_point_mutation(wt, 3, "A"))
```
---
# Citation

If you use this model, please cite:

> **Chiara Rodella & Thomas Lemmin**  
> *H3BERTa: A CDR-H3 specific language model for antibody repertoire analysis*  
> Institute of Biochemistry and Molecular Medicine, University of Bern (Switzerland) (under review)

---

#  License

The model and tokenizer are released under the MIT License.
For commercial or large-scale applications, please contact the authors to discuss licensing or collaboration.

---


