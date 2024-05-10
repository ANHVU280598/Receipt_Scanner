import re

patern1 = r'^[A-Za-z]{3}\s\d{1,2}$'
patern2 = r'^\d{2}/\d{2}$'

def precheck_date_character_format(string): # Matches "Aug 15" format
    return re.match(patern1, string) is not None  

def precheck_month_day_num_format(string): #Matches "08/18" format
    return re.match(patern2, string) is not None 

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def extract_transactions_from_text(text):
    valid_format = False
    trans_date = None
    transactions = []
    lines = text.split("\n")
    for line in lines:
        parts = line.split()
        # Check if the line contains all necessary parts
        if len(parts) >= 6:
            # Extract Transaction Date, Post Date, Description, and Amount
            trans_date1 = " ".join(parts[:1])
            trans_date2 = " ".join(parts[:2])
          
            start_index = 2

            if  precheck_month_day_num_format(trans_date1):
                trans_date = trans_date1
                valid_format = True

            if precheck_date_character_format(trans_date2):
                trans_date = trans_date2
                valid_format = True
                start_index = 3

            if not valid_format:
                continue

            if parts[-2] =='-':
               description = " ".join(parts[start_index:-2])
               amount = " ".join(parts[-2:]) 
            else:
                description = " ".join(parts[start_index:-1])
                amount = parts[-1]
        
            if(is_float(amount.replace(",", "").replace("$", "").replace(" ",""))):
                amount = float(amount.replace(",", "").replace("$", "").replace(" ",""))
                transactions.append({
                        "Trans Date": trans_date,
                        "Description": description,
                        "Amount": amount
                    })
    return transactions