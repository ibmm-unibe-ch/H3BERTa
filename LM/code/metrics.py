from Bio.Align import substitution_matrices
import torch


def calculate_blosum_score(amino1, amino2, blosum_matrix,scores):
    #print('BLOSUM COUPLE', amino1,amino2)
    try:
        scores.append(blosum_matrix[(amino1, amino2)])
    except KeyError:
        # if the couple of aa it is not present in the matrix
        scores.append(-5)  
    except IndexError:
        # if the couple of aa contains one [UNK]
        scores.append(-5)  
    return scores

def calculate_blosum_scores(predicted_sequences, original_sequences):
    '''
    blosum_scores = calculate_blosum_scores(predicted_values, true_values)
    average_blosum_score = sum(blosum_scores) / len(blosum_scores)
    print("Val AVG Blosum for all amino acids:", average_blosum_score)
    '''
    #from Bio.SubsMat import MatrixInfo #in in the older biopython version
    #blosum_matrix = MatrixInfo.blosum62
    blosum_matrix  = substitution_matrices.load('BLOSUM62')
    scores = []
    for pred_seq, orig_seq in zip(predicted_sequences, original_sequences):
        '''per amino acids couple, not per sequence in this case, 
        double check if you want to compute it per sequences pair'''
        calculate_blosum_score(pred_seq, orig_seq, blosum_matrix,scores)
    return scores


def calculate_pppl(input_id): #edited
    '''
    ppls = torch.tensor([])
    input_ids = batch.input_ids[i]
    ppl_batch = torch.tensor(list(map(calculate_pppl, input_ids))) # i remove the ppl computation since it will call the model for each sequence len(seq) times, no feasible for training/validation purpose
    ppls = torch.cat([ppls,ppl_batch])
    '''
    #token_ids = tokenizer.encode(sequence, return_tensors='pt')
    token_ids = input_ids.unsqueeze(0)
    input_length = token_ids.size(1)
    log_likelihood = 0.0

    for i in range(input_length):
        # Create a copy of the token IDs
        masked_token_ids = token_ids.clone()
        # Mask a token that we will try to predict back
        masked_token_ids[0, i] = tokenizer.mask_token_id

        with torch.no_grad():
            output = model(masked_token_ids)
            logit_prob = torch.nn.functional.log_softmax(output.logits, dim=-1)
        
        log_likelihood += logit_prob[0, i, token_ids[0, i]]

    # Calculate the average log likelihood per token
    avg_log_likelihood = log_likelihood / input_length

    # Compute and return the pseudo-perplexity
    pppl = torch.exp(-avg_log_likelihood)
    return pppl.item()