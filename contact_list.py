from numpy import number
import pandas as pd
from openpyxl import load_workbook
from zipfile import ZipFile

df = pd.read_excel('D:\\VS CODE\\Project\\main.py\\contacts.xlsx')

name = input("name : ")
print(df["name"])

for a in df:
    if (name != a[0]):
        print("your name is not saved in contacts")
        num = input("Number : ")
        df1 = pd.DataFrame(name)
        w1 = pd.ExcelWriter('contacts.xlsx', engine='xlsxwriter')
        df.to_excel(w1, sheet_name='contacts.xlsx', index=False)
        df1.to_excel(w1, sheet_name='contacts.xlsx', index=False, header=False, startrow=len(df)+1)
        w1.save()
        break
    else:
        break
