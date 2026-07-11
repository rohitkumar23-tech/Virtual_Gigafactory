import os 
import pandas as pd

def validate_file(file_path):
    valid,err=file_exists(file_path)
    if not valid:
        return False,err
    valid,err=is_csv(file_path)
    if not valid:
        return False,err 
    valid,err=is_empty(file_path)
    if not valid:
        return False,err   
    return True, None
        
def file_exists(file_path):
    exist=os.path.exists(file_path)
    if exist:
        return True, None
    else:
        return False,"File does not exist"

def is_csv(file_path): 
    if file_path.endswith(".csv"):
        return True, None
    else:
        return False,"The file is not a csv file"

def is_empty(file_path):
    try:
        data=pd.read_csv(file_path)
        if not data.empty:
            return True, None
        else:
            return False,"The file is empty"
    except Exception:
        return False,"Unable to read the CSV file"
    
def has_required_coloumns(file_path):
    try:  
        clm=['Voltage','Current','Temperature']
        data=pd.read_csv(file_path) 
        for header in clm:
            if header not in data.columns:
                return False,f"{header} does not exist"
            return True,None
    except Exception:
        return False,"Unable to read the CSV"

