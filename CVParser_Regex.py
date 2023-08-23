# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:58:15 2023

@author: EA
"""

import re
from PyPDF2 import PdfReader

def pdf_to_text(pdf_path):
    pdf = PdfReader(pdf_path)
    return ' '.join([page.extract_text() for page in pdf.pages])

def extract_emails(text):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    return emails

def extract_phone_numbers(text):
    pattern = r'(\d{3}) (\d{3}) (\d{2}) (\d{2})'
    pattern_second = r'(\d{3})-(\d{3})-(\d{2})-(\d{2})'
    pattern_third = r'(\d{11})'
    pattern_fourth = r'(\d{10})'

    match = re.search(pattern, text)
    match_second = re.search(pattern_second, text)
    match_third = re.search(pattern_third, text)
    match_fourth = re.search(pattern_fourth, text)

    if match:
        return match.group()
    elif match_second:
        return match_second.group()
    elif match_third:
        return match_third.group()
    elif match_fourth:
        return match_fourth.group()
    else:
        return "Phone pattern not found"
    
def extract_names(text):
    names = re.findall(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b', text)
    return names

def main():
    pdf_path = "pdfparsel_ornek3.pdf"
    text = pdf_to_text(pdf_path)

    emails = extract_emails(text)
    phone_number = extract_phone_numbers(text)
    names = extract_names(text)

    print("Emails:")
    for email in emails:
        print(email)

    print("Phone Number:", phone_number)
    
    print("Names:")
    for name in names:
        print(name)

if __name__ == "__main__":
    main()