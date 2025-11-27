# Funzione per calcolare la perplexity of an MLM
def calculate_pseudo_perplexity(sequence, model, tokenizer):
    import torch
    from tqdm import tqdm
    
    """
    This function calculates the perplexity of a given sequence using a masked language model (MLM).

    Perplexity is a measure of how well a language model predicts a sequence. Lower perplexity indicates better performance.

    Parameters:
        sequence (str): The input text sequence for which to compute perplexity.
        model (transformers.PreTrainedModel): The pre-trained masked language model.
        tokenizer (transformers.PreTrainedTokenizer): The tokenizer corresponding to the MLM.

    Steps:
    1. Tokenize the input sequence into tokens compatible with the model, returning input IDs and an attention mask.
    2. Initialize an empty list to store the log-probabilities of each token in the sequence.
    3. For each token in the sequence:
        - Create a masked version of the sequence by replacing the current token with the model's mask token.
        - Pass the masked sequence to the model to get the logits (predicted probabilities) for the masked token.
        - Extract the probability of the true token (the token at the masked position) from the logits.
        - Compute the log of this probability and append it to the list.
    4. Compute the average log-probability across all tokens in the sequence.
    5. Calculate the perplexity by taking the exponential of the negative average log-probability.
    6. Return the perplexity value as a float.

    Returns:
        float: The perplexity of the input sequence.

    Note:
    - The function uses `torch.no_grad()` to avoid computing gradients, which is unnecessary for inference.
    - The model's predictions are conditioned on the context provided by the rest of the sequence.
    """

    # Check if CUDA is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    tokens = tokenizer(sequence, return_tensors="pt")
    input_ids = tokens.input_ids.to(device)
    attention_mask = tokens.attention_mask.to(device)

    log_probabilities = []
    # Get the list of special tokens
    special_tokens = tokenizer.all_special_ids  # Or alternatively, use the specific IDs for special tokens

    with torch.no_grad():
        # Use tqdm for the loop with a progress bar
        for i in range(input_ids.shape[1]): 
            # Skip special tokens
            if input_ids[0, i].item() in special_tokens:
                continue

            # Create a copy of the sequence and mask the current token
            masked_input_ids = input_ids.clone().to(device)
            masked_input_ids[0, i] = tokenizer.mask_token_id

            # Get the model's predictions
            outputs = model(masked_input_ids, attention_mask=attention_mask)
            logits = outputs.logits

            # Calculate the probability of the correct token
            token_logits = logits[0, i]
            true_token_id = input_ids[0, i]
            token_prob = torch.softmax(token_logits, dim=-1)[true_token_id]

            # Calculate the logarithm of the probability
            log_probabilities.append(torch.log(token_prob))

    # Calculate the perplexity
    avg_log_prob = torch.stack(log_probabilities).mean()
    perplexity = torch.exp(-avg_log_prob)
    return perplexity.cpu().item()

