# Dataset Creation

## 0. RAW UNPAIRED
We took all the Bcells available for healthy patient data and load them in a local OAS SQLite3  database. The search yielded **1,863,590,990** unique sequences from **34** studies

Some different data pipelines have been tested:
- SUB-PIPELINE1: only IgG and IgA with all the Bsources
- SUB-PIPELINE2: only IgG and IgA with Unsorted B cells
- SUB-PIPELINE3: all isotypes with all the Bsources
- SUB-PIPELINE4: all isotypes with Unsorted B cells

In this repository we report the pipeline described in the paper: (SUB-PIPELINE1) only IgG and IgA with all the Bsources
## 1. FOR EACH SUB-PIPELINE:

**Main folder** : `./SUB-PIPELINE.../`
##### 1. Extract CDRH3 from OAS database 

Inside each sub-pipeline folder, the code has been customized to retrieve the specific data we want:

:
```
```bash
./code/1_extract_cdr3.sh 
```
For each pipeline, it will create the following files:
* `1_cdrh3_part1.csv`
* `1_cdrh3_part2.csv`
* `1_cdrh3_part1.fasta`
* `1_cdrh3_part2.fasta`

We have part 1 and part 2 because the data were too large, so we split them into two databases:

- OAS_heavy_part1.db
- OAS_heavy_part2.db
##### 2. Merge and prepare the data
Remove header lines in the FASTA files and the first line in the CSV file, then merge the part1 and part2 files and rename the main file. Delete unnecessary files.

```bash
./code/2_merge_cdrh3_files
```
##### 3. Run mmseqs linclust with different pident
Do not include '1_cdrh3.fasta', just use '1_cdrh3' since the code will already be searching for .fasta files.

```bash
./code/3_cluster_cdrh3.sh
```

#####  4. PIDENT selection (70) + data cleaning (optional centroids full heavy sequence retrieving)

The code calls `../src/CDRH3_Xpident.sh` to select the desired percentage identity (pident), clean the data by removing loops with more than two 'XX' and loops shorter than three amino acids, and then clusters the data at 30% pident for splitting into training, testing, and validation sets. We are working with 70 pident. The script `../src/CDRH3_Xpident.sh` also includes a commented section for retrieving the full sequences of CDRH3 centroids if needed.

```bash
./code/4_X_cdrh3_pident.sh
```

#####  4. Train-val-test splitting and data preparation in the `5_TRAINING_SETS` folder.
This script splits the dataset in ~80-10-10, keeping larger clusters for the training set, and reformats the output into CSV files with Hugginface required headers (id,text). It then organizes the generated files into a directory named `5_TRAINING_SETS`.

```bash
./code/5_train_val_test_split.sh
```
