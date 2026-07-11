def generate_report(pipeline_stats):
    print("---------Pipeline Report---------")
    print(f"Total Files      ={pipeline_stats['total_files']}")
    print(f"Failed Files     ={len(pipeline_stats['failed_files'])}")
    print(f"Successful Count ={pipeline_stats['successful_count']}")
    print(f"Time Taken       ={pipeline_stats['total_time']}")
    for file_name,error in pipeline_stats["failed_files"]:
        print(f'File name: {file_name}--> Error:{error}')

