#!/bin/bash

# Remove header lines in the FASTA files and the first line in the CSV file
sed -i '1d' 1_cdrh3_2.csv
sed -i '1,2d' 1_cdrh3_1.fasta
sed -i '1,2d' 1_cdrh3_2.fasta
echo "Headers removed from 1_cdrh3_2.csv, 1_cdrh3_1.fasta, and 1_cdrh3_2.fasta"

# Merge the files
cat 1_cdrh3_2.csv >> 1_cdrh3_1.csv
echo "Files 1_cdrh3_2.csv and 1_cdrh3_1.csv merged"

cat 1_cdrh3_2.fasta >> 1_cdrh3_1.fasta
echo "Files 1_cdrh3_2.fasta and 1_cdrh3_1.fasta merged"

# Rename the main files
mv 1_cdrh3_1.csv 1_cdrh3.csv
mv 1_cdrh3_1.fasta 1_cdrh3.fasta
echo "Files renamed to 1_cdrh3.csv and 1_cdrh3.fasta"

# Delete unnecessary files
rm 1_cdrh3_2.csv
rm 1_cdrh3_2.fasta
echo "Unnecessary files 1_cdrh3_2.csv and 1_cdrh3_2.fasta deleted"
