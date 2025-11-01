#!/bin/bash
#SBATCH --dependency=afterok:23946

## extract rowid and cdrh3 in csv and fasta format (for the clustering)
sqlite3 -header -csv /ibmm_data2/oas_database/OAS_heavy_part1.db "SELECT ROWID,cdr3_aa,Isotype,BSource,BType FROM human_unpaired_novaccine_nodisease_heavy WHERE Isotype IN ('IGHG', 'IGHA')  AND Vaccine IS 'None' AND Disease IS 'None';" | tee >(awk -F, '{print ">"$1"\n"$2}' > 1_cdrh3_1.fasta) > 1_cdrh3_1.csv


sqlite3 -header -csv /ibmm_data2/oas_database/OAS_heavy_part2.db "SELECT ROWID,cdr3_aa,Isotype,BSource,BType FROM human_unpaired_novaccine_nodisease_heavy WHERE Isotype IN ('IGHG', 'IGHA')  AND Vaccine IS 'None' AND Disease IS 'None';" | tee >(awk -F, '{print ">"$1"\n"$2}' > 1_cdrh3_2.fasta) > 1_cdrh3_2.csv




