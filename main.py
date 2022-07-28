import requests
from constants import API_REQUEST_REGISTRO_LIST, API_REQUEST_MANT_SKELETON, TypeFields, NameFields, records, Campos
from api.googlesheet import sheet
from api.zinkee import getData
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

    nameCampos = [NameFields]
    
    content = getData(response_json, records, TypeFields, Campos)

    request=sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=sheetName+"!A:Z").execute()
    
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=sheetName+"!A1",valueInputOption="USER_ENTERED",body={"values":nameCampos}).execute()
    
    request=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=sheetName+"!A2",valueInputOption="USER_ENTERED",body={"values":content}).execute()
    
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=sheetName+"!A:Z").execute()

    values = result.get('values', [])
    print(values)

