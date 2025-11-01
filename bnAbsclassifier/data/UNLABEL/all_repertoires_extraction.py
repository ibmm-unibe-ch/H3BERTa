#!mkdir ./repertoires/all_repertoires/
import pandas as pd
import tqdm

# AUTOMATIZE EXTRACTION OF ALL THE REPERTOIRES

##### HEALTHY

# # Carica il file meta_data
# meta_data = pd.read_csv('PRJNA486667_SraRunTable.txt')
# meta_data = meta_data[meta_data['disease'] == 'HIV Negative']

# # Carica il file HIV_NEG
# hp = pd.read_csv('HIV_NEG/HIV_NEG.tsv', sep='\t')

# # Pulizia del dataset
# hp = hp.dropna(subset=['cdr3_aa'])
# #hp = hp.drop_duplicates(subset=['cdr3_aa'])

# # Splitting 'sequence_id' into 'Run' and 'index'
# hp[['Run', 'index']] = hp['sequence_id'].str.split('.', expand=True)

# # Ottieni tutti i soggetti unici
# subjects = meta_data['subject'].unique()

# for subject in tqdm.tqdm(subjects):
#     # Ottieni la lista dei 'Run' associati a quel soggetto
#     healthy_repertoire = meta_data[meta_data['subject'] == subject].Run.tolist()

#     # Filtra il dataset hp in base ai 'Run' corrispondenti
#     subject_hp = hp[hp['Run'].isin(healthy_repertoire)].copy()
    
#     # Aggiungi la colonna 'label'
#     subject_hp['label'] = 'NON'
    
#     # Salva il file con il nome del soggetto
#     output_filename = f'./repertoires/all_repertoires/healthy_repertoire_withcdrh3duplicates_{subject}.txt'
#     subject_hp[['sequence_id', 'cdr3_aa', 'label','v_identity','d_identity','j_identity','v_family', 'd_family','j_family',	'c_family']].to_csv(output_filename, index=False, header=None)

#     print(f"File salvato: {output_filename}")


##### BNABS


# # Carica il file meta_data
# meta_data = pd.read_csv('PRJNA486667_SraRunTable.txt')
# meta_data = meta_data[meta_data['disease'] == 'HIV Broad Neutralizing']

# # Carica il file HIV_NEG
# hp = pd.read_csv('HIV_BNABS/HIV_BNABS.tsv',sep='\t', )

# # Pulizia del dataset
# hp = hp.dropna(subset=['cdr3_aa'])
# #hp = hp.drop_duplicates(subset=['cdr3_aa'])

# # Splitting 'sequence_id' into 'Run' and 'index'
# hp[['Run', 'index']] = hp['sequence_id'].str.split('.', expand=True)

# # Ottieni tutti i soggetti unici
# subjects = meta_data['subject'].unique()

# for subject in tqdm.tqdm(subjects):
#     # Ottieni la lista dei 'Run' associati a quel soggetto
#     healthy_repertoire = meta_data[meta_data['subject'] == subject].Run.tolist()

#     # Filtra il dataset hp in base ai 'Run' corrispondenti
#     subject_hp = hp[hp['Run'].isin(healthy_repertoire)].copy()
    
#     # Aggiungi la colonna 'label'
#     subject_hp['label'] = 'BRO'
    
#     # Salva il file con il nome del soggetto
#     output_filename = f'./repertoires/all_repertoires/bnabs_repertoire_withcdrh3duplicates_{subject}.txt'
#     subject_hp[['sequence_id', 'cdr3_aa', 'label','v_identity','d_identity','j_identity','v_family', 'd_family','j_family',	'c_family']].to_csv(output_filename, index=False, header=None)

#     print(f"File salvato: {output_filename}")


##### NEUTRALIZERS

# Carica il file meta_data
meta_data = pd.read_csv('PRJNA486667_SraRunTable.txt')
meta_data = meta_data[meta_data['disease'] == 'HIV Non Neutralizing']

# Carica il file HIV_NEG
hp = pd.read_csv('HIV_NON/HIV_NON.tsv',sep='\t', )

# Pulizia del dataset
hp = hp.dropna(subset=['cdr3_aa'])
#hp = hp.drop_duplicates(subset=['cdr3_aa'])

# Splitting 'sequence_id' into 'Run' and 'index'
hp[['Run', 'index']] = hp['sequence_id'].str.split('.', expand=True)

# Ottieni tutti i soggetti unici
subjects = meta_data['subject'].unique()

for subject in tqdm.tqdm(subjects):
    # Ottieni la lista dei 'Run' associati a quel soggetto
    healthy_repertoire = meta_data[meta_data['subject'] == subject].Run.tolist()

    # Filtra il dataset hp in base ai 'Run' corrispondenti
    subject_hp = hp[hp['Run'].isin(healthy_repertoire)].copy()
    
    # Aggiungi la colonna 'label'
    subject_hp['label'] = 'NEU'
    
    # Salva il file con il nome del soggetto
    output_filename = f'./repertoires/all_repertoires/neutralizers/neu_repertoire_withcdrh3duplicates_{subject}.txt'
    subject_hp[['sequence_id', 'cdr3_aa', 'label','v_identity','d_identity','j_identity','v_family', 'd_family','j_family',	'c_family']].to_csv(output_filename, index=False, header=None)

    print(f"File salvato: {output_filename}")