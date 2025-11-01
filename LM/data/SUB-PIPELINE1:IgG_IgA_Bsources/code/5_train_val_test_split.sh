#!/bin/bash

# Split the data keeping clusters together (bigger clusters-->train set)
python ../src/train_test_val_split.py \
--tsv_dataset ./4_CDRH3_70pident/30PIDENT_SPLITTING/4_cdrh3_70_rep_clean_30_clu.tsv \
--rep_id_seq_file ./4_CDRH3_70pident/4_cdrh3_70_rep_clean.csv \
--prefix SB1

# Create the directory 5_TRAINING_SETS if it doesn't already exist
mkdir -p 5_TRAINING_SETS

# Add headers and reformat the train files into CSV format
# The run_mlm_no_trainer.py script will use the column called 'text' or the first column if no column called 'text' is found.
# Since we are in the ids,sequence format, I will add the header line and also change their format to CSV.

awk 'BEGIN {print "id,text"} {print}' SB1_train.txt > 5_TRAINING_SETS/train.csv 
awk 'BEGIN {print "id,text"} {print}' SB1_val.txt > 5_TRAINING_SETS/val.csv
awk 'BEGIN {print "id,text"} {print}' SB1_test.txt > 5_TRAINING_SETS/test.csv

# Move all files that start with 'SB' into the directory 5_TRAINING_SETS
mv SB* 5_TRAINING_SETS/



