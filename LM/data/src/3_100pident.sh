#!/bin/bash

mkdir 3_100CDRH3pident
# Removing sequences with more than 2 X aa
awk -F',' '{if ($2 !~ /X.*X.*X/) print $0}' ./2_clustering/1_cdrh3_100_clu_rep_idseq_noduplicates > ./3_100CDRH3pident/1_cdrh3_100_clu_rep_idseq_noduplicates_noXX 

# Removing sequences shorter than 3 aa
awk -F',' 'length($2) >= 3' ./3_100CDRH3pident/1_cdrh3_100_clu_rep_idseq_noduplicates_noXX > ./3_100CDRH3pident/3_cdrh3_100_rep_clean.csv

# Extract cdrh3 centroids ids 
awk -F',' '{ print $1}' ./3_100CDRH3pident/3_cdrh3_100_rep_clean.csv > ./3_100CDRH3pident/3_cdrh3_100_rep_clean_ids

# Create fasta file with the centroids sequences
awk -F',' '{print ">"$1"\n"$2}' ./3_100CDRH3pident/3_cdrh3_100_rep_clean.csv > ./3_100CDRH3pident/3_cdrh3_100_rep_clean.fasta

# cluster the 100 cdrh3 centroids with pident 50
./code/mmseqs_linclust.sh /ibmm_data/rodelc/DALM/HEAVY/CDRH3/LM/HEALTHY/data/3_100CDRH3pident/3_cdrh3_100_rep_clean.fasta

# import cdrh3 centroids as table in the .db
sqlite3 /ibmm_data2/oas_database/OAS_heavy.db ".import /ibmm_data/rodelc/DALM/HEAVY/CDRH3/LM/HEALTHY/data/3_100CDRH3pident/3_cdrh3_100_rep_clean_ids cdrh3_100_rep_clean_ids" 

# extract the full heavy sequence of each centroids from the database
sqlite3 -header -csv /ibmm_data2/oas_database/OAS_heavy.db  "SELECT ROWID,cdr3_aa,sequence_alignment_aa FROM Bcells_subset_human_unpaired_heavy WHERE ROWID IN (SELECT ROWID FROM cdrh3_100_rep_clean_ids);" > ./3_100CDRH3pident/3_100CDRH3rep_heavyseqs.csv

# create a fasta with heavy sequences
awk -F',' '{print ">"$1"\n"$3}' 3_100CDRH3pident/3_100CDRH3rep_heavyseqs.csv > 3_100CDRH3pident/3_100CDRH3rep_heavyseqs.fasta



