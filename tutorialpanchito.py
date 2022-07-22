import pandas as pd
import requests 
import openpyxl

#LEER excel

archivo_excel = pd.read_excel("supermarket_sales.xlsx")
print(archivo_excel[[""]])