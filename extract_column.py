import schedule 
import time
import pandas as pd 
from Ex_Col.logger import logging
from Ex_Col.exception import ExcelException

def extract_columns():
    try:
        print("Hello i am extracting excel's columns")
        excel_path = r'C:\Users\Admin\Downloads\CS675-22531-Spring-2023-Assignments.xlsx'
        df = pd.read_excel(excel_path)
        columns_to_extract = ['Last_Name','First_Name','Asgn-01']
        extracted_columns = df[columns_to_extract]
        # Save the extracted columns to a new Excel file
        extracted_columns.to_excel(r'c:\Users\Admin\Desktop\extracted_columns.xlsx', index=False)
    except Exception as e:
        logging.error(f"{e}")
        print(e)

schedule.every(10).seconds.do(extract_columns)
while 1:
    schedule.run_pending()
    time.sleep(1)