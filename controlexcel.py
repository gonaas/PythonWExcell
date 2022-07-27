from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
from openpyxl import Workbook
import numpy as np
import pandas as pd

stage = "https://www.backend.stage.zinkee.com:8443/MasaBackend-stage"

apiRegistros = "/api/mant/registro/list"
apiCampos = "/api/mant/skeleton/get"
app = "121"
apiKey = "97A2B1D5-D266-41C4-B5A8-20BEB45A2D2F"
math = "2"

#Variable request mannt/registro
registros = []
Campos = []

#Variable request mannt/skeleton
VectorTipos = []
VectorId = []
VectorNombre= []

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
            elif((VectorTipos[n] == "N")):
                Campos.append(reg["data"][n]["valor"]["number"])
            elif((VectorTipos[n] == "D")):
                try:
                    if((reg["data"][n]["valorRel"])==  None):
                            try:
                                Campos.append(reg["data"][n]["valor"]["number"])
                            except:
                                Campos.append(reg["data"][n]["valor"])
                    else:
                        Campos.append(reg["data"][n]["valorRel"])
                        
                except:
                        Campos.append(reg["data"][n]["valor"]["numberFixed"])
            elif((VectorTipos[n] == "U") or (VectorTipos[n] == "LV") or (VectorTipos[n] == "UG") or (VectorTipos[n] == "RM")):
                Campos.append(reg["data"][n]["valorRel"])
            else:
                Campos.append("-")

            
    VCampos = np.array(Campos)
    MCampos = np.reshape(VCampos, (len(registros), len(VectorTipos)))
    

    #API GOOGLE SHEET
    
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # ID = ((URL spreadsheet - */d) - /edit*)
    # The ID spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1lRIDShBQU1oe7WOi6Q3FeuOCBvrAp02-A3_LhgwZ6Zs'

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    
    request=sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="test2!A:Z").execute()
    
    nameCampos = [VectorNombre]
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="test2!A1",valueInputOption="USER_ENTERED",body={"values":nameCampos}).execute()
    content = MCampos.tolist()
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range="test2!A2",valueInputOption="USER_ENTERED",body={"values":content}).execute()

    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="test2!A:Z").execute()

    values = result.get('values', [])
    print(values)

