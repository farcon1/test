import xlwt
import openpyxl
from openpyxl import load_workbook

wb = openpyxl.load_workbook(filename = "test1/ex.xlsx")
sheet = wb['my_sheet']    
sheet["A1"].value="12345678910"
wb.save()
print(sheet["A1"].value)