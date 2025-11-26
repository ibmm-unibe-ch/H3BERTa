# Dataset Creation

## 0. RAW UNPAIRED

We collected all **B-cell** sequences from **healthy donor datasets** available in the [OAS repository](https://opig.stats.ox.ac.uk/webapps/oas/)and loaded them into a local **SQLite3 database**. 

The OAS local database is split into **part1** and **part2** due to size constraints, resulting in two SQLite databases:  
- `OAS_heavy_part1.db`  
- `OAS_heavy_part2.db`  
The search yielded **1,863,590,990 unique sequences** across **34 studies**.

Several alternative data pipelines were evaluated:

- **SUB-PIPELINE1:** IgG and IgA, all B-cell sources  
- **SUB-PIPELINE2:** IgG and IgA, *Unsorted* B cells only  
- **SUB-PIPELINE3:** All isotypes, all B-cell sources  
- **SUB-PIPELINE4:** All isotypes, *Unsorted* B cells only  

> The dataset used in the paper corresponds to **SUB-PIPELINE1** (IgG and IgA, all B-cell sources).

---

## 1. FOR EACH SUB-PIPELINE

**Main folder:**  
```
./SUB-PIPELINE.../
```

### 1. Extract CDRH3 sequences from OAS database  

Each sub-pipeline folder contains a customized script to retrieve the desired subset of data:

```bash
./code/1_extract_healthy_cdr3.sh
```

This script generates the following files:  
- `1_cdrh3_part1.csv`  
- `1_cdrh3_part2.csv`  
- `1_cdrh3_part1.fasta`  
- `1_cdrh3_part2.fasta`  

---

### 2. Merge and prepare the data  

Remove header lines from FASTA files and the first line from CSV files.  
Then merge the parts and rename the final combined file.  
Temporary files are deleted automatically.

```bash
./code/2_merge_cdrh3_files
```

---

### 3. Cluster with MMseqs (linclust)  

Run MMseqs2 **linclust** using various *pident* thresholds.  
Do not include the file extension — use `1_cdrh3` instead of `1_cdrh3.fasta`, as the script automatically appends the extension.

```bash
./code/3_cluster_cdrh3.sh
```

---

### 4. PIDENT selection (70%) and optional data cleaning  

The script below calls `../src/CDRH3_Xpident.sh` to:
- Select the desired **percentage identity** (70% used in the paper)  
- Remove sequences with >2 “XX” or loops shorter than 3 amino acids  
- Optionally retrieve full heavy-chain sequences for CDRH3 centroids (commented section in the script)  
- Perform a secondary clustering at 30% identity for train/validation/test splitting  

```bash
./code/4_X_cdrh3_pident.sh
```

---

### 5. Train/validation/test splitting  

Splits the clustered dataset into approximately **80/10/10** proportions, prioritizing larger clusters for the training set.  
Outputs are reformatted into CSV files compatible with **Hugging Face** headers (`id,text`), and stored in:

```
./5_TRAINING_SETS/
```

```bash
./code/5_train_val_test_split.sh
```

---

### Notes  

Due to **GitHub storage limitations**, the dataset files are hosted separately on **Zotero**.  
They can also be **recreated locally** once a copy of the OAS database is available, by executing the scripts in `/code` in the order described above.
