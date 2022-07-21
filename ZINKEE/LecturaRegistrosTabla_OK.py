import requests
import json

if __name__ == '__main__':
    url = 'https://www.backend.zinkee.com:8443/MasaBackend/api/mant/registro/list'
    payload = {'mantId':'77', 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    headers = {'App' : '65', 'Content-Type' : 'application/json', 'Authorization': '3B35DEBE-79B8-4CFE-AD8A-E95F2CEA2783'}
    response = requests.post(url, headers=headers, json=payload)

    contador = 1
    reg = 0
    
    response_json = response.json()
    for registro in response_json:
        print("\nRegistro ", contador)
        print("Campo Texto:")
        print(response_json[reg]["data"][0]["valor"])
        print("Campo Num:")
        print(response_json[reg]["data"][1]["valor"]["number"])      
        print("Campo Num Con Form:")
        print(response_json[reg]["data"][2]["valor"]["number"])
        print("Fecha:")
        print(response_json[reg]["data"][3]["valor"])
        contador += 1
        reg += 1
    
    