#!/bin/bash

# Define the disease data array
disease_data=("HIV_BNABS" "HIV_NON" "HIV_NEG")

# Loop through each element in the array
for i in "${disease_data[@]}"
do
    echo "Processing: $i"  # Print the current element being processed
    cd "$i" || continue  # Change directory to the current disease_data element; continue to the next if directory doesn't exist

    # Run your script or command here
    ../download_fastq_fasta_from_accession_list.sh "${i}"*

    cd ..  # Return to the parent directory
done

