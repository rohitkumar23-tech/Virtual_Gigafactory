from validator import validate_file
from reader import read_file 

file_path="../raw_data/formation_batch_001.csv"
valid,err=validate_file(file_path)
if not valid:
    print(err)
    exit()

data=read_file(file_path)
print(data['Current'])
