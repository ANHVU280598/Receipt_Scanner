import re

def is_month_day(string):
    # Define a regex pattern for month and day combination (e.g., "Aug 15")
    pattern = r'^[A-Za-z]{3}\s\d{1,2}$'
    # Check if the string matches the pattern
    return re.match(pattern, string) is not None

def extract_transactions_from_text(text):
    transactions = []
    lines = text.split("\n")
    for line in lines:
        # Split each line by whitespace
        parts = line.split()
        # print(parts)
        # Check if the line contains all necessary parts
        if len(parts) >= 6:
            # Extract Transaction Date, Post Date, Description, and Amount
            trans_date = " ".join(parts[:2])
            post_date = " ".join(parts[2:4])
            if parts[-2] =='-':
               description = " ".join(parts[4:-2])
               amount = " ".join(parts[-2:])
            else:
                description = " ".join(parts[4:-1])
                amount = parts[-1]
            
            # Append the extracted data as a dictionary
            if is_month_day(trans_date) and is_month_day(post_date):
                transactions.append({
                    "Trans Date": trans_date,
                    "Post Date": post_date,
                    "Description": description,
                    "Amount": amount
                })
    return transactions