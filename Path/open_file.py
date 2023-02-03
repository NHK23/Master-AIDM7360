import pandas as pd
import os, pathlib

# complete full folder path
def file_path(file_name):
    folder_path = os.getcwd()
    check_sql_path(folder_path)
    full_path = folder_path + '/' + 'Data' + '/' + file_name
    return full_path


# check folder path whether exist
def check_sql_path(dataPath):
    if not(os.path.exists(dataPath)):
    # os.mkdir(dataPath) 
    # Creates only the last directory if missing. Rises error if it exists
        path = pathlib.Path(dataPath)
        path.mkdir(parents=True, exist_ok=True)             # Can create the folders in the path if missing. No error if path exists
    else:
        print('The data path you selected already exists')


# open csv file and put it into dataframe
def csv_read(csv_name):
    csv_path = file_path(csv_name)
    #try:
    temp_df = pd.read_csv(csv_path, low_memory = False, encoding= 'unicode_escape')
    # except Exception as ex:
    #     print(ex)
    
    return temp_df


# create sql path
def sql_path(sql_name):
    sql_path = file_path(sql_name)
    print(sql_path)
    return sql_path


# create report file path
def report_path(report_name):
    report_path = file_path('report/'+ report_name)
    print(report_path)
    file = open(report_path, 'w') 
    file.write('')
    return report_path