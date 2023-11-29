import pandas as pd
import requests
import json
import os

url = "https://api.knack.com/v1/objects/object_1/records"
headers = {
    "X-Knack-Application-Id": "65291e6ecec047002915c63c",
    "X-Knack-REST-API-Key": "1776bd3c-c198-46bc-9b92-fac0acab8424"
}

response = requests.get(url, headers=headers)


if response.status_code == 200:

    data = json.loads(response.text)
    record  = data [ 'records' ]
    Cycle = input("Please enter the Cycle you are working on " "\n")
    Month = input("Please enter the Month "  "\n")
    fpath = r"C:\Users\Shiva\Data\Python\Web\Scrapping"
    foldername = "E-billing_" + Cycle + "_" + Month
    folder = os.path.join(fpath,foldername)
    filepath = folder + "\\"
    if not os.path.isdir(folder):
        os.mkdir(folder)
    else:
        print("Your folder already exist")   
    for i in record:
        if i['field_3'] == Cycle and i['field_4'] == Month :             
            with open(filepath+i['field_2_raw']+"_"+i['field_4_raw']+"_"+i['field_3']+"_"+i['id']+".xlsx","wb") as f:
                f.write(requests.get(i['field_6_raw']['url']).content)
    list_files = os.listdir(folder)
    finaldf = pd.DataFrame()
    if len(list_files) > 1:
        combinefolder = os.path.join(fpath, "combined_file\\")
        if not os.path.isdir(combinefolder):
            os.mkdir(combinefolder)
        else:
            print("You have a combine folder too")
        for f in list_files:
            if f.endswith(".xlsx"):
                df = pd.read_excel(filepath+f)   
                df1 = df.fillna("")
                df2 = df1.rename(columns={" ":""})
                df3 = df2.rename(columns={"Cost ID":"Time ID","Extra Time":"Extra Time Taken","Matter ID":"MatterID", "Admin Comments": "Additional Comment Regarding Attorneys Feedback","TotalCost":"TotalFees","QTY":"Hours", "Qty1":"Hours1", "ProformaDate":"ProformaPrintDate"})      
                finaldf = finaldf._append(df3)
        finalexcel =  combinefolder +"Combined_"+Cycle+"_"+Month+".xlsx"   
        print(finaldf)
        finaldf.to_excel(finalexcel, index=False)

    else:
        print("You do not have any file yet or have only one file.")
else:
    print(f"Request failed with status code {response.status_code}")

