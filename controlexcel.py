import requests
import json
import openpyxl as xl

stage = "https://backend.stage.zinkee.com:8443/MasaBackend-stage"
api = "/api/mant/registro/list"
app = "65"
apiKey = "3B35DEBE-79B8-4CFE-AD8A-E95F2CEA2783"
math = "77"

if __name__ == '__main__':
    url = stage + api
    payload = {'mantId': math, 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    headers = {'App' : app, 'Content-Type' : 'application/json', 'Authorization': apiKey}
    response = requests.post(url, headers=headers, json=payload)

    fila = 2
    reg = 0
    
    response_json = response.json()
    data = response_json[reg]["data"][1]
        print(data + "\n")
    
    '''
    for registro in response_json:
        columna = 1
        
        c_texto = response_json[reg]["data"][0]["valor"]
        c_num = response_json[reg]["data"][1]["valor"]["number"]
        c_numf = response_json[reg]["data"][2]["valor"]["number"]
        c_fecha = response_json[reg]["data"][3]["valor"]
        f_creacion = response_json[reg]["data"][4]["valor"]
        u_creador = response_json[reg]["data"][5]["valorRel"]
        
        #Datos a excel
        archivo = xl.load_workbook('excel.xlsx')
        hoja = archivo['Hoja1'] 
        
        ex_c_texto = hoja.cell(fila, columna)
        ex_c_texto.value = c_texto
        archivo.save('excel2.xlsx')
        
        #Suma fila y columna || 
        fila += 1
        reg += 1
        
    print('Correcto')
    '''