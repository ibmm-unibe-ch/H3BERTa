#!/bin/bash

# Specify the desired percentage identity (pident) to retain, clean the data
# (removing loops with more than 2 'XX' and loops shorter than 3 amino acids),
# then cluster the data at 30% pident for splitting into training, testing, and validation sets.

../src/CDRH3_Xpident.sh 70



