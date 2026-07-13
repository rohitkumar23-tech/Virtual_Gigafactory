import logging
from config import log_file,folder_path,Processed_data_folder
from validator import validate_file
from reader import read_file 
import os
import time
from reporter import generate_report
from writer import write_file
import transformer
logging.basicConfig(filename=log_file,
                    level=logging.INFO, 
                    format="%(asctime)s,%(levelname)s,%(message)s"
                    )

pipeline_stats={
    'failed_files':[],
    'successful_files':[],
    'total_files':0,
    'total_time':0,
    'rows_removed':0,
    'rows_written':0,
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
    data,rows_read,rows_removed,rows_written=transformer.remove_missing_rows(data)
    pipeline_stats['rows_removed']+=rows_removed
    pipeline_stats['rows_written']+=rows_written
    pipeline_stats['successful_files'].append({'file_name':file_name,
                                              'rows_read':rows_read, 
                                              'rows_removed':rows_removed,
                                              'rows_written':rows_written})
    name,extension=os.path.splitext(file_name)
    output_path=os.path.join(Processed_data_folder,f"{name}_processed{extension}")
    write_file(data,output_path)

    print(data['Current'])

end_time=time.time()
pipeline_stats['total_time']=end_time-start_time
generate_report(pipeline_stats)



