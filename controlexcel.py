import requests
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

stage = "https://backend.stage.zinkee.com:8443/MasaBackend-stage"
apiRegistros = "/api/mant/registro/list"
apiCampos = "/api/mant/skeleton/get"
app = "65"
apiKey = "3B35DEBE-79B8-4CFE-AD8A-E95F2CEA2783"
math = "77"

wb = Workbook()
sheet = wb.active
sheet.title = "Plantillas CS math77"
registros = []
Campos = []

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
            if((VectorTipos[n] == "T") or (VectorTipos[n] == "F") or (VectorTipos[n] == "H")):
                Campos.append(reg["data"][n]["valor"])
            elif((VectorTipos[n] == "N")):
                Campos.append(reg["data"][n]["valor"]["number"])
            elif((VectorTipos[n] == "U")):
                Campos.append(reg["data"][n]["valorRel"])
    '''''
    indexvector = 0
    for row in range(0, len(registros)):
        for col in range(0, len(VectorTipos)):
            x[row][col] = Campos[indexvector]
            indexvector +=1
    '''''

        
    print(VectorNombre)
    print(VectorTipos)
    print(VectorId)
    print(Campos)     
    print(len(Campos))   
    
