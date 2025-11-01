#!/bin/bash

sratoolkit_path='/home/rodelc/sratoolkit.3.0.7-ubuntu64/bin/'
acc_numbers_file=$1

while IFS= read -r i || [[ -n "$i" ]]; do
    "$sratoolkit_path"prefetch "$i"
    "$sratoolkit_path"fasterq-dump "$i" --split-files
    cat "$i".fastq | awk '{if(NR%4==1) {printf(">%s\n",substr($0,2));} else if(NR%4==2) print;}' > "$i".fasta
    rm -r "$i"
    rm "$i".fastq
done < $acc_numbers_file

