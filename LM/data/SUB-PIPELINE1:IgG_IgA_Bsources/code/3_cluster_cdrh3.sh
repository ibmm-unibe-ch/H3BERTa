#!/bin/bash

# Cluster the CDR-H3 loops running the clustering script using MMseqs2 Linclust (the input file must be named 1_cdrh3.fasta)

mkdir 3_CLUSTERING
cd ./3_CLUSTERING
../../src/mmseqs_linclust.sh ../1_cdrh3



