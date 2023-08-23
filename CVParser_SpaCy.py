# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:58:47 2023

@author: EA
"""

import spacy
from PyPDF2 import PdfReader

nlp = spacy.load("xx_ent_wiki_sm")

def pdf_to_text(pdf_path):
    pdf = PdfReader(pdf_path)
    return ' '.join([page.extract_text() for page in pdf.pages])

def extract_names(text):
    doc = nlp(text)
    full_names = []
    for ent in doc.ents:
        print(ent.text, ent.label_)  
        if ent.label_ == "PERSON":  
            full_names.append(ent.text)
    return full_names

def main():
    pdf_path = "pdfparsel_ornek6.pdf"
    text = pdf_to_text(pdf_path)

    full_names = extract_names(text)

    print("Full Names:")
    for name in full_names:
        print(name)

if __name__ == "__main__":
    main()