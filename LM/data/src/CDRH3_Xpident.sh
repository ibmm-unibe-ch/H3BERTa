#!/bin/bash

P=$1

echo "Creating directory 4_CDRH3_${P}pident..."
mkdir 4_CDRH3_"$P"pident
echo "Directory 4_CDRH3_${P}pident created."

# Removing sequences with more than 2 X aa
echo "Removing sequences with more than 2 X amino acids..."
awk -F',' '{if ($2 !~ /X.*X.*X/) print $0}' ./3_CLUSTERING/1_cdrh3_"$P"_clu_rep_idseq_noduplicates > ./4_CDRH3_"$P"pident/1_cdrh3_"$P"_clu_rep_idseq_noduplicates_no2XX 
echo "Sequences with more than 2 X amino acids removed."


# Removing sequences shorter than 3 aa
echo "Removing sequences shorter than 3 amino acids..."
awk -F',' 'length($2) >= 3' ./4_CDRH3_"$P"pident/1_cdrh3_"$P"_clu_rep_idseq_noduplicates_no2XX > ./4_CDRH3_"$P"pident/4_cdrh3_"$P"_rep_clean.csv
echo "Sequences shorter than 3 amino acids removed."

# Extract cdrh3 centroids ids 
echo "Extracting cdrh3 centroids ids..."
awk -F',' '{ print $1}' ./4_CDRH3_"$P"pident/4_cdrh3_"$P"_rep_clean.csv > ./4_CDRH3_"$P"pident/4_cdrh3_"$P"_rep_clean_ids
echo "cdrh3 centroids ids extracted."

# Create fasta file with the centroids loops sequences
echo "Creating fasta file with the centroids loops sequences..."
awk -F',' '{print ">"$1"\n"$2}' ./4_CDRH3_"$P"pident/4_cdrh3_"$P"_rep_clean.csv > ./4_CDRH3_"$P"pident/4_cdrh3_"$P"_rep_clean.fasta
echo "Fasta file with centroids sequences created."

# cluster the "$P" cdrh3 centroids with pident 30 (for train test val splitting)
echo "Creating directory 30PIDENT_SPLITTING..."
mkdir ./4_CDRH3_"$P"pident/30PIDENT_SPLITTING/
echo "Directory 30PIDENT_SPLITTING created."


echo "Changing to 50PIDENT_SPLITTING directory and running clustering script..."
cd ./4_CDRH3_"$P"pident/30PIDENT_SPLITTING/
../../../src/mmseqs_linclust_train_test_val.sh ../4_cdrh3_"$P"_rep_clean
echo "Clustering script executed."

echo "Returning to previous directory..."
cd ..
echo "Script completed."

# import cdrh3 centroids as table in the .db
#sqlite3 /ibmm_data2/oas_database/OAS_heavy.db ".import /ibmm_data/rodelc/DALM/HEAVY/CDRH3/LM/HEALTHY/data/3_100CDRH3pident/3_cdrh3_100_rep_clean_ids cdrh3_100_rep_clean_ids" 

# extract the full heavy sequence of each centroids from the database
#sqlite3 -header -csv /ibmm_data2/oas_database/OAS_heavy.db  "SELECT ROWID,cdr3_aa,sequence_alignment_aa FROM Bcells_subset_human_unpaired_heavy WHERE ROWID IN (SELECT ROWID FROM cdrh3_100_rep_clean_ids);" > ./3_100CDRH3pident/3_100CDRH3rep_heavyseqs.csv

# create a fasta with heavy sequences
#awk -F',' '{print ">"$1"\n"$3}' 4_CDRH3_100pident/3_100CDRH3rep_heavyseqs.csv > 4_CDRH3_100pident/3_100CDRH3rep_heavyseqs.fasta



