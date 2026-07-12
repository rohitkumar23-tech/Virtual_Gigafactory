import logging
from config import log_file,folder_path,Processed_data_filepath
from validator import validate_file
from reader import read_file 
import os
import time
from reporter import generate_report
logging.basicConfig(filename=log_file,
                    level=logging.INFO, 
                    format="%(asctime)s,%(levelname)s,%(message)s"
                    )

pipeline_stats={
    'failed_files':[],
    'successful_files':[],
    'total_files':0,
    'total_time':0
}
directory_files=os.listdir(folder_path) 
start_time=time.time()
for file_name in directory_files:
    file_path=os.path.join(folder_path,file_name)
    valid,err=validate_file(file_path)
    pipeline_stats['total_files']+=1
    if not valid:
        pipeline_stats['failed_files'].append((file_name,err))
        print(err)
        continue

    data=read_file(file_path)
    pipeline_stats['successful_files'].append(file_name)
    print(data['Current'])

end_time=time.time()
pipeline_stats['total_time']=end_time-start_time
generate_report(pipeline_stats)



