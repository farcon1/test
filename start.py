import xlwt
import openpyxl as opx
from openpyxl import load_workbook

wb = openpyxl.load_workbook(filename = "ex.xlsx")
sheet = wb['my_sheet']    
sheet["A1"].value="12345678910"
wb.save()
print(sheet["A1"].value)