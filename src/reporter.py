from config import report_width
def print_section(text):
        print(f"{'-'*report_width}\n")
        print(f"{text.center(report_width)}\n")
        print(f"{'-'*report_width}\n")
def generate_report(pipeline_stats):
    
    total_files=pipeline_stats['total_files']
    failed_files=pipeline_stats['failed_files']
    successful_files=pipeline_stats['successful_files']
    time_taken=pipeline_stats['total_time']
    rows_removed=pipeline_stats['rows_removed']
    rows_written=pipeline_stats['rows_written']

    title="PIPELINE SUMMARY"
    print(f"{'='*report_width}\n") 
    print(f"{title.center(report_width)}\n")
    print(f"{'='*report_width}")
    print_section("Summary")
    print(f"Total Files      ={total_files}")
    print(f"Failed Files     ={len(failed_files)}")
    print(f"Successful Files ={len(successful_files)}")
    print(f"Time Taken       ={time_taken:.2f} seconds")
    print_section("Row Transformation summary")

    for files in successful_files:
        print(f'File name:                 {files['file_name']}')
        print(f'Total Read rows count:     {files['rows_read']}')
        print(f'Total Removed rows count:  {files['rows_removed']}')
        print(f'Total Written rows count:  {files['rows_written']}')
               
        
    
    print_section("Failed Files")
    if not failed_files:
        print("There are no failed files.")
    else:
        for file_name,error in failed_files:
            print(f'File name: {file_name}: Error:{error}\n')


    

