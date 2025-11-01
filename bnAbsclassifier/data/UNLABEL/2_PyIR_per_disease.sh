#!/bin/bash

# 2.5 h run
# Define the disease data array
disease_data=("HIV_BNABS" "HIV_NON" "HIV_NEG")

# Loop through each element in the array
for i in "${disease_data[@]}"
do
    echo "Processing: $i"  # Print the current element being processed
    cd "$i" || continue  # Change directory to the current disease_data element; continue to the next if directory doesn't exist

    # merge all the fasta
    cat *.fasta > "$i".fasta
    
    #pyir
    pyir  "$i".fasta --multi 58 --outfmt 'tsv'

    cd ..  # Return to the parent directory
done

