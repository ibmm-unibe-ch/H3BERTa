#!/bin/bash

# Define the disease data array
disease_data=("HIV_BNABS" "HIV_NON" "HIV_NEG")
log_file="cdrh3_redundancy_log.txt"  # Log file to store the output

# Loop through each element in the array
for i in "${disease_data[@]}"
do
    echo "Processing: $i" >> "$log_file"  # Log the current element being processed

    cd "$i" || continue  # Change directory to the current disease_data element; continue to the next if directory doesn't exist
    echo "All data in $i.tsv:" >> "../$log_file"
    wc -l "$i".tsv >> "../$log_file"  # Print the line before the awk command
    # removing overlaps in the cdrh3 loops 
    awk -F'\t' 'NR==1 { for(i=1; i<=NF; i++) if($i=="cdr3_aa") col=i; } !seen[$col]++' "$i".tsv > "$i"_noredundancyh3.tsv
    echo "After keeping unique cdrh3 in $i.tsv:" >> "../$log_file"
    wc -l "$i"_noredundancyh3.tsv >> "../$log_file"  # Print the line after the awk command
    
    echo "----------------------------------------------------------------" >> "../$log_file"
    cd ..  # Return to the parent directory
done

