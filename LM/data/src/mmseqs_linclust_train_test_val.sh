#!/bin/bash

# Check if the number of arguments passed to the script is not equal to 1
if [ "$#" -ne 1 ]; then
    echo "DATA: $1 DB "
    exit 1
fi

# Assign the input database name (DB) to the first argument passed to the script
DB="$1"
echo "DATA: $0 DB "



# Create a log file to record the output of operations
log_file="$DB""_mmseqs_linclust.log"
echo "Log saved to: $log_file"

# Count the number of sequences in the input file and record it in the log file
db_rows=$(grep -o ">" "$DB".fasta | wc -l)
echo "Number of sequences in $DB.fasta: $db_rows" > "$log_file"
echo "" >> "$log_file"


# Create an MMseqs2 database using the input file "$DB.fasta" and save it with the same name as "$DB", --dbtype 1 == Aminoacids
mmseqs createdb "$DB".fasta "$(basename "$DB")" --dbtype 1

DB="$(basename "$DB")"

echo "#####################################################################################################################################"  >> "$log_file"
# Define an array containing the desired percentage identity thresholds
# 30 : 20% or 30% would be the lower limit for homology modeling
minseqid=(0.3)
pident_int=(30)


# Iterate over each threshold value and perform clustering
for ((i = 0; i < ${#minseqid[@]}; i++)); do
    p=${minseqid[$i]}
    pident=${pident_int[$i]}

    # Perform clustering using MMseqs2 (linclust) with the specified minimum sequence identity threshold
    mmseqs linclust "$DB" "${DB}_${pident}_clu" tmp --min-seq-id "$p"

    # Create a sub-database of representative sequences from the clusters
    mmseqs createsubdb "${DB}_${pident}_clu" "$DB" "${DB}_${pident}_clu_rep" 

    # Convert the representative sub-database to FASTA format
    mmseqs convert2fasta "${DB}_${pident}_clu_rep" "${DB}_${pident}_clu_rep.fasta"

    # Create a TSV file mapping the input sequences to the clusters they belong to
    mmseqs createtsv "$DB" "$DB" "${DB}_${pident}_clu" "${DB}_${pident}_clu.tsv"

    # Extract unique IDs from the representative sequence file and remove duplicates
    awk '/^>/ { printf("\n%s,", substr($0, 2)); next; } { printf("%s", $0);} END { printf("\n"); }' "${DB}_${pident}_clu_rep.fasta" > "${DB}_${pident}_clu_rep_idseq"
    awk -F ',' '!seen[$2]++' "${DB}_${pident}_clu_rep_idseq" > "${DB}_${pident}_clu_rep_idseq_noduplicates"

    # Count the number of rows in TSV and representative sequence files, the number of unique sequences, and the number of rows after removing duplicates
    clu_rows=$(wc -l < "${DB}_${pident}_clu.tsv")
    rep_rows=$(wc -l < "${DB}_${pident}_clu_rep_idseq")
    unique_sequences=$(cut -d ',' -f 2 "${DB}_${pident}_clu_rep_idseq" | sort | uniq | grep -c "")
    rep_rows_noduplicates=$(wc -l < "${DB}_${pident}_clu_rep_idseq_noduplicates")

    # Print clustering information including row counts and unique sequence counts to the log file
    echo "${pident} CLUSTERING, ${p} MINSEQID" >> "$log_file"
    echo "DATA: $0 DB " >> "$log_file"
    echo "Number of rows in ${DB}_${pident}_clu.tsv: $clu_rows" >> "$log_file"
    echo "Number of rows in ${DB}_${pident}_clu_rep_idseq: $rep_rows" >> "$log_file"
    echo "Number of unique centroids sequences in the second column: $unique_sequences" >> "$log_file"
    echo "Number of rows in ${DB}_${pident}_clu_rep_idseq_noduplicates after removing duplicates: $rep_rows_noduplicates" >> "$log_file"
    echo "" >> "$log_file"
done

# Remove the temporary directory "tmp" used during execution
rm -r tmp

# rename the file to be consistent with the step 2 of the pipeline
mv "$log_file"  3_cdrh3_mmseqs_linclust_SPLITTING.log
