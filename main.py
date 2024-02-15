import torch
from collections import Counter
import random
import re

file_path = 'dataset/black_hole_wiki.txt'

# Open the file and read its content
with open(file_path, 'r') as file:
    file_content = file.read()

raw_text = file_content

def add_start_end_sentence(text):
    return "start-of-sentence " + text.replace("."," end-of-sentence start-of-sentence")


def remove_citations(text):
    pattern = r"\[\d+\]"
    cleaned_text = re.sub(pattern, "", text)    
    return cleaned_text

def remove_spaces(text):
    pattern = r"\s+"
    cleaned_text = re.sub(pattern, " ", text)    
    return cleaned_text

def preprocess(text: str):
    return remove_spaces(remove_citations(add_start_end_sentence(text).lower().replace(" s ","").replace("\\","").replace("'"," ").replace('"',' ').replace(","," ").replace("\ s"," ").replace("\n"," ")))

preprocessed_text = preprocess(raw_text)

Counter(preprocessed_text.split(" ")).most_common(20)

preprocessed_text_array = preprocessed_text.split(" ")


print(preprocessed_text_array[0:10])

