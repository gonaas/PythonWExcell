import requests
import json
from openpyxl import Workbook


if __name__ == '__main__':
    url = 'https://backend.stage.zinkee.com:8443/MasaBackend-stage/api/mant/registro/list'
    payload = {'mantId':'77', 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    headers = {'App' : '65', 'Content-Type' : 'application/json', 'Authorization': '3B35DEBE-79B8-4CFE-AD8A-E95F2CEA2783'}
    response = requests.post(url, headers=headers, json=payload)

    fila = 2
    reg = 0
    
    response_json = response.json()
    for registro in response_json:
        columna = 1
        
        c_texto = response_json[reg]["data"][0]["valor"]
        c_num = response_json[reg]["data"][1]["valor"]["number"]
        c_numf = response_json[reg]["data"][2]["valor"]["number"]
        c_fecha = response_json[reg]["data"][3]["valor"]
        f_creacion = response_json[reg]["data"][4]["valor"]
        u_creador = response_json[reg]["data"][5]["valorRel"]
        
        #Datos a excel
        wb = Workbook()
        sheet = wb.active
        sheet.title = "Plantillas CS math77"
        
        ex_c_texto = sheet.cell(fila, columna)
        print(c_texto)
        print(c_num)
        ex_c_texto.value = c_texto
        wb.save('excel2.xlsx')
        
        #Suma fila y columna || 
        fila += 1
        reg += 1
        
    print('Correcto')
    