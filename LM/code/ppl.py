from transformers import AutoModelForMaskedLM, AutoTokenizer
import torch

def calculate_pppl(model, tokenizer, sequence):
    token_ids = tokenizer.encode(sequence, return_tensors='pt')
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

# Load the model and tokenizer
model_name = "facebook/esm2_t12_35M_UR50D"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained(model_name)

# Protein sequence
protein_sequence = "MKTIIALSYIFCLVFA"

# Calculate PPPL
pppl = calculate_pppl(model, tokenizer, protein_sequence)
print(f"Pseudo-Perplexity of the sequence: {pppl}")

