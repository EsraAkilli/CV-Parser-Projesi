# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:59:26 2023

@author: EA
"""

import re
from collections import Counter
from PyPDF2 import PdfReader
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def pdf_to_text(pdf_path):
    pdf = PdfReader(pdf_path)
    return ' '.join([page.extract_text() for page in pdf.pages])

def extract_names(text):
    words = word_tokenize(text)
    
    capitalized_words = [word for word in words if word[0].isupper()]
    
    name_combinations = []
    for i in range(len(capitalized_words) - 1):
        name_combinations.append(f"{capitalized_words[i]} {capitalized_words[i + 1]}")
    
    name_counter = Counter(name_combinations)
    
    full_names = []
    for name, count in name_counter.items():
        if count >= 1 and len(name) > 1:
            full_names.append(name) 
            break 
    
    return full_names

def main():
    pdf_path = "pdfparsel_ornek3.pdf"
    text = pdf_to_text(pdf_path)

    full_names = extract_names(text)

    if full_names:
        print("First Full Name Found:")
        print(full_names[0])
    else:
        print("No full name found.")

if __name__ == "__main__":
    main()
