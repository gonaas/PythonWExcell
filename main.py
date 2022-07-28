import requests
import numpy as np
from constants import API_REQUEST_REGISTRO_LIST, API_REQUEST_MANT_SKELETON, TypeFields, NameFields, records, Campos
from api.googlesheet import sheet
from seetings import stage, app, apiKey, math, sheetName, SAMPLE_SPREADSHEET_ID

if __name__ == '__main__':
    
    url = stage + API_REQUEST_REGISTRO_LIST
    urlCampos = stage + API_REQUEST_MANT_SKELETON
    
    payload = {'mantId': math, 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    payloadCampos = {'mantId': math}
    
    headers = {'App' : app, 'Content-Type' : 'application/json', 'Authorization': apiKey}
    
    response = requests.post(url, headers=headers, json=payload)
    responseCampos = requests.post(urlCampos, headers=headers, json=payloadCampos)

    response_json = response.json()
    response_json_campos = responseCampos.json()
    
    for cam in response_json_campos["campos"]:
        TypeFields.append(cam["tipo"])
        NameFields.append(cam["nombre"])

    for reg in response_json:
        records.append(reg["id"])
        for n in range (0, len(reg["data"])):
            if((TypeFields[n] == "T") or (TypeFields[n] == "F") or (TypeFields[n] == "H")or (TypeFields[n] == "B") or (TypeFields[n] == "V")):
                Campos.append(reg["data"][n]["valor"])
            elif((TypeFields[n] == "N")):
                Campos.append(reg["data"][n]["valor"]["number"])
            elif((TypeFields[n] == "D")):
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
            elif((TypeFields[n] == "U") or (TypeFields[n] == "LV") or (TypeFields[n] == "UG") or (TypeFields[n] == "RM")):
                Campos.append(reg["data"][n]["valorRel"])
            else:
                Campos.append("-")

            
    VCampos = np.array(Campos)
    MCampos = np.reshape(VCampos, (len(records), len(TypeFields)))
    

    request=sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheetName+"!A:Z").execute()
    nameCampos = [NameFields]
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=sheetName+"!A1",valueInputOption="USER_ENTERED",body={"values":nameCampos}).execute()
    content = MCampos.tolist()
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=sheetName+"!A2",valueInputOption="USER_ENTERED",body={"values":content}).execute()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=sheetName+"!A:Z").execute()

    values = result.get('values', [])
    print(values)

