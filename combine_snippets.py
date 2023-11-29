import os
import pandas as pd
import shutil
from datetime import date

today = date.today()
stoday = today.strftime("%m-%y-%d")
current_path = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(current_path,'E-billing')
folder = os.path.join(current_path,'combined_file')
pdffilemove = os.path.join(current_path,'Back_ups',stoday)

print(pdffilemove)
print(stoday)

if not os.path.isdir(folder):
    os.mkdir(folder)
else:
    print("Your folder already exist")   
    list_files = os.listdir(filepath)
    finaldf = pd.DataFrame()
    if len(list_files) > 1: 
        if not os.path.isdir(pdffilemove):
            os.mkdir(pdffilemove)       
        for f in list_files:
            if f.endswith(".xlsx"):
                combinedfilename = os.path.join(folder, f)
                pdffilepath = os.path.join(filepath, f)
                df = pd.read_excel(pdffilepath)   
                df1 = df.fillna("")
                df2 = df1.rename(columns={" ":""})
                df3 = df2.rename(columns={"Cost ID":"Time ID","Extra Time":"Extra Time Taken","Matter ID":"MatterID", "Admin Comments": "Additional Comment Regarding Attorneys Feedback","TotalCost":"TotalFees","QTY":"Hours", "Qty1":"Hours1", "ProformaDate":"ProformaPrintDate","Matter Number":"MatterID","Additional Comment Regarding Attorneys Feddback":"Additional Comment Regarding Attorneys Feedback"})      
                finaldf = finaldf._append(df3)
                shutil.move(pdffilepath,pdffilemove)
        combinedfilename = "combined.xlsx"
        finalexcel =  os.path.join(folder, combinedfilename)
        finaldf.to_excel(finalexcel, index=False)
    else:
        print("You do not have any file yet or have only one file.")
