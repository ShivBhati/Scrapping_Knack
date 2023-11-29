import os
import pandas as pd
import shutil

filepath = r'B:\Python\Web\Scrapping\E-billing_1_Oct'
folder = r'B:\Python\Web\Scrapping\combined_file'
pdffilemove = r'B:\Python\Web\Scrapping\Back_ups'

if not os.path.isdir(folder):
    os.mkdir(folder)
else:
    print("Your folder already exist")   
    list_files = os.listdir(filepath)
    finaldf = pd.DataFrame()
    if len(list_files) > 1:        
        for f in list_files:
            if f.endswith(".xlsx"):
                combinedfilename = os.path.join(folder, f)
                pdffilepath = os.path.join(filepath, f)
                pdffilemovepath = os.path.join(pdffilemove,f)
                df = pd.read_excel(pdffilepath)   
                df1 = df.fillna("")
                df2 = df1.rename(columns={" ":""})
                df3 = df2.rename(columns={"Cost ID":"Time ID","Extra Time":"Extra Time Taken","Matter ID":"MatterID", "Admin Comments": "Additional Comment Regarding Attorneys Feedback","TotalCost":"TotalFees","QTY":"Hours", "Qty1":"Hours1", "ProformaDate":"ProformaPrintDate"})      
                finaldf = finaldf._append(df3)
                shutil.move(pdffilepath,pdffilemovepath)
        combinedfilename = "combined.xlsx"
        finalexcel =  os.path.join(pdffilemovepath, combinedfilename)
        finaldf.to_excel(finalexcel, index=False)
    else:
        print("You do not have any file yet or have only one file.")
