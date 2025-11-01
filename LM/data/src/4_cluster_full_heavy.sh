#!/bin/bash

# cluster the heavy chains of the 100 pident cdrh3 centroids
mkdir 4_clustering_heavy_seqs
cd 4_clustering_heavy_seqs
../code/mmseqs_linclust.sh /ibmm_data/rodelc/DALM/HEAVY/CDRH3/LM/HEALTHY/data/3_100CDRH3pident/3_100CDRH3rep_heavyseqs

