#!/bin/bash

# Set the directory where the scripts are located
SCRIPT_DIR="/ibmm_data/rodelc/DALM/CLS_bnAbs/CDRH3/GAN-BERT_TRAININGS/no_IMV/H3BERTA/src_model_evaluation"

# Check if the directory exists
if [ ! -d "$SCRIPT_DIR" ]; then
    echo "The directory $SCRIPT_DIR does not exist."
    exit 1
fi

# Run the scripts in sequence using their full path, while remaining in the current directory
"$SCRIPT_DIR"/1.test_set_val_set_testing_BRO_NON_embeddings_output.sh
"$SCRIPT_DIR"/2.outputs_cleaning.sh
"$SCRIPT_DIR"/3.dimensionality_reduction.sh
"$SCRIPT_DIR"/3.dimensionality_reduction_complete.sh
"$SCRIPT_DIR"/4.addiotional_plots.sh
#"$SCRIPT_DIR"/5.all_IMV_repertoires.sh
#"$SCRIPT_DIR"/6.IMV_to_test.sh
"$SCRIPT_DIR"/7.SOTA:rain.sh
"$SCRIPT_DIR"/8.test_on_IMV_labeled_data.sh
