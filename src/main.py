import os
import pandas as pd
data=pd.read_csv("../raw_data/formation_batch_001.csv")
print (data["Current"])
files=os.listdir("../raw_data")
print(os.chdir("../raw_data"))
count=0
for file in files:
    if file.endswith(".csv"):
        print(file)
        count+=1
print("found",count,"CSV Files")