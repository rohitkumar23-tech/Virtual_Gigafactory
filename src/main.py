import logging
from config import log_file,folder_path,Processed_data_filepath
from validator import validate_file
from reader import read_file 
import os
import time
logging.basicConfig(filename=log_file,
                    level=logging.INFO, 
                    format="%(asctime)s,%(levelname)s,%(message)s"
                    )

failed_files=[]
successful_count=0
directory_files=os.listdir(folder_path)
start_time=time.time()
for file_name in directory_files:
    file_path=os.path.join(folder_path,file_name)
    valid,err=validate_file(file_path)
    if not valid:
        failed_files.append((file_name,err))
        print(err)
        continue

    data=read_file(file_path)
    successful_count+=1
    print(data['Current'])

end_time=time.time()
total_time=end_time-start_time

