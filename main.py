from PyPDF2 import PdfReader
import re
import os
from extractTextFromPdf import extract_text_from_pdf
from extractTransactionFromText import extract_transactions_from_text

directory = 'BankStatements'
files = os.listdir(directory)

all_transactions = []

def group_transactions_by_description(transactions):
    grouped_transactions = {}
    for transaction in transactions:
        description = transaction['Description']
        first_three_letters = description[:6]
        if first_three_letters in grouped_transactions:
            grouped_transactions[first_three_letters].append(transaction)
        else:
            grouped_transactions[first_three_letters] = [transaction]
    return grouped_transactions


for file in files:
    if file.endswith('.pdf'):
        # Construct the full file path
        filepath = os.path.join(directory, file)


        pdf_text = extract_text_from_pdf(filepath)

        transactions = extract_transactions_from_text(pdf_text)

        all_transactions.extend(transactions)
        # sorted_transactions = sorted(all_transactions, key=lambda x: x['Trans Date'])

        # # Print transaction details sorted by 'Trans Date'
        # for i, transaction in enumerate(sorted_transactions, 1):
        #     print(f"Transaction {i}:")
        #     print(f"Trans Date: {transaction['Trans Date']}")
        #     print(f"Description: {transaction['Description']}")
        #     print(f"Amount: {transaction['Amount']}")
        #     print()
sorted_transactions = sorted(all_transactions, key=lambda x: x['Trans Date'])
grouped_transactions = group_transactions_by_description(sorted_transactions)




for key, value in grouped_transactions.items():
    print(f"Transactions with description starting with '{key}':")
    for i, transaction in enumerate(value, 1):
        print(f"Transaction {i}: {transaction}")
    print()
