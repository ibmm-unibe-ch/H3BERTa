#!/bin/bash

mkdir 3_70HEAVYpident

# Extract cdrh3 centroids ids 
awk -F',' '{ print $1}' ./4_clustering_heavy_seqs/3_100CDRH3rep_heavyseqs_70_clu_rep_idseq_noduplicates > ./3_70HEAVYpident/100CDRH3rep_70HEAVYrep_ids

# Create fasta file with the centroids sequences
awk -F',' '{print ">"$1"\n"$2}' ./4_clustering_heavy_seqs/3_100CDRH3rep_heavyseqs_70_clu_rep_idseq_noduplicates > ./3_70HEAVYpident/3_cdrh3_100_rep_clean.fasta

# import cdrh3 centroids as table in the .db
sqlite3 /ibmm_data2/oas_database/OAS_heavy.db ".import /ibmm_data/rodelc/DALM/HEAVY/CDRH3/LM/HEALTHY/data/3_100CDRH3pident/3_cdrh3_100_rep_clean_ids 100CDRH3rep_70HEAVYrep_ids" 

# extract the full heavy sequence of each centroids from the database
sqlite3 -header -csv /ibmm_data2/oas_database/OAS_heavy.db  "SELECT ROWID,cdr3_aa,sequence_alignment_aa FROM Bcells_subset_human_unpaired_heavy WHERE ROWID IN (SELECT ROWID FROM cdrh3_100_rep_clean_ids);" > ./3_100CDRH3pident/3_100CDRH3rep_heavyseqs.csv

# create a fasta with heavy sequences
awk -F',' '{print ">"$1"\n"$3}' 3_100CDRH3pident/3_100CDRH3rep_heavyseqs.csv > 3_100CDRH3pident/3_100CDRH3rep_heavyseqs.fasta
