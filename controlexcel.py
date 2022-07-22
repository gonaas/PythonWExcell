import requests
from openpyxl import Workbook
import numpy as np
import pandas as pd
import xlsxwriter

stage = "https://backend.stage.zinkee.com:8443/MasaBackend-stage"
apiRegistros = "/api/mant/registro/list"
apiCampos = "/api/mant/skeleton/get"
app = "65"
apiKey = "3B35DEBE-79B8-4CFE-AD8A-E95F2CEA2783"
math = "31"

#Variable request mannt/registro
registros = []
Campos = []

#Variable request mannt/skeleton
VectorTipos = []
VectorId = []
VectorNombre= []

x = [[]]

if __name__ == '__main__':
    
    url = stage + apiRegistros
    urlCampos = stage + apiCampos
    
    payload = {'mantId': math, 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    payloadCampos = {'mantId': math}
    
    headers = {'App' : app, 'Content-Type' : 'application/json', 'Authorization': apiKey}
    
    response = requests.post(url, headers=headers, json=payload)
    responseCampos = requests.post(urlCampos, headers=headers, json=payloadCampos)

    response_json = response.json()
    response_json_campos = responseCampos.json()

    for cam in response_json_campos["campos"]:
        VectorId.append(cam["id"])
        VectorTipos.append(cam["tipo"])
        VectorNombre.append(cam["nombre"])

    for reg in response_json:
        registros.append(reg["id"])
        for n in range (0, len(reg["data"])):
            
            if((VectorTipos[n] == "T") or (VectorTipos[n] == "F") or (VectorTipos[n] == "H")or (VectorTipos[n] == "B") or (VectorTipos[n] == "V")):
                Campos.append(reg["data"][n]["valor"])
            elif((VectorTipos[n] == "N") or (VectorTipos[n] == "D")):
                Campos.append(reg["data"][n]["valor"]["numberFixed"])
            elif((VectorTipos[n] == "U") or (VectorTipos[n] == "LV") or (VectorTipos[n] == "UG") or (VectorTipos[n] == "RM")):
                Campos.append(reg["data"][n]["valorRel"])
            else:
                Campos.append("-")
            
    VCampos = np.array(Campos)
    MCampos = np.reshape(VCampos, (len(registros), len(VectorTipos)))
    
    print(MCampos)
    print(VectorNombre)
    print(registros)
    print(Campos)
    
    archivo = xlsxwriter.Workbook("porfavor.xlsx")
    hoja = archivo.add_worksheet()
    
    for n in range(0, len(VectorNombre)):
        hoja.write(0,n,VectorNombre[n])
    
    for row in range(1, len(registros)):
        for col in range(0,len(VectorNombre)):
            hoja.write(row,col,MCampos[row][col])
            
    
    archivo.close()
    
