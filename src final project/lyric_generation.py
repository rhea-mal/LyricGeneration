import pandas as pd
import numpy as np
import torch
from transformers import get_linear_schedule_with_warmup
from torch.optim import AdamW
from tqdm import tqdm  # For progress bars
from torch.utils.data import DataLoader, Dataset
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import os

def remove_standalone_pre(text):
    updated_text = text.replace(' pre ', ' ')
    if updated_text.startswith('pre '):
        updated_text = updated_text[4:]
    if updated_text.endswith(' pre'):
        updated_text = updated_text[:-4]

    return updated_text

def feature_based_generation(model, tokenizer, feature_string, device):
    """
    Generate lyrics based on structured features and a prompt.

    Args:
    - model: The trained GPT model.
    - tokenizer: The tokenizer used for the GPT model.
    - features: A dictionary containing the features and their values.
    - device: The device ('cuda' or 'cpu') to perform the computation on.

    Returns:
    - The generated lyrics as a string.
    """

    input_sequence = f"{feature_string} <LYRICS>:"
    inputs = tokenizer.encode(input_sequence, return_tensors='pt').to(device)

    output_sequences = model.generate(
        input_ids=inputs,
        max_length=512,
        min_length=50,
        num_beams=5,
        no_repeat_ngram_size=2,
        early_stopping=True,
        temperature=0.9, 
        top_k=50, 
        top_p=0.92, 

    )
    lyrics = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return remove_standalone_pre(lyrics)

def process_librosa_input(segment_feature_string):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    new_path = script_dir[:-3]
    model_load_path = new_path + 'models/gpt2_lyrics_model_50_epochs'
    tokenizer_load_path = new_path + 'models/gpt2_lyrics_tokenizer_50_epochs'

    model = GPT2LMHeadModel.from_pretrained(model_load_path)

    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_load_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    generated_lyrics = feature_based_generation(model, tokenizer, segment_feature_string, device)
    lyrics_index = generated_lyrics.find("<LYRICS>: ")
    final_output = generated_lyrics[lyrics_index + len("<LYRICS>: "):]
    return final_output
