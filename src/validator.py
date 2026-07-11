
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
    data=pd.read_csv(file_path)
    if not data.empty:
        return True, None
    else:
        return False,"The file is empty"

