#Remove rows containing missing values  and return the cleaned data
def remove_missing_rows(data):
    cleaned_data=data.dropna()
    rows_read=data.shape[0]
    rows_written=cleaned_data.shape[0]
    rows_removed=rows_read-rows_written
    return cleaned_data,rows_read,rows_removed,rows_written