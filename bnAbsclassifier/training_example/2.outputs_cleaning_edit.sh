#!/bin/bash

mkdir outputs/

mkdir outputs/3_22_24_IMV_LAB
mv 3_22_24* outputs/3_22_24_IMV_LAB

mkdir outputs/healthy_repertoire_700010189
mv healthy_repertoire*  outputs/healthy_repertoire_700010189

mkdir outputs/hiv_repertoire_700010333
mv hiv_repertoire*  outputs/hiv_repertoire_700010333

mkdir outputs/label_test
mv binary_50pident_test* outputs/label_test

mkdir outputs/label_val
mv binary_50pident_val* outputs/label_val


mkdir outputs/label_train
mv binary_50pident_train* outputs/label_train

mkdir outputs/3_22_24_with_duplicates

mv patient_repertoire_3_22_24* outputs/3_22_24_with_duplicates
