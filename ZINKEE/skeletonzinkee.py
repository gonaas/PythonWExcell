import requests

if __name__ == '__main__':
    url = 'https://www.backend.zinkee.com:8443/MasaBackend/api/mant/registro/list'
    payload = {'mantId':'103', 'mantVistaId':'null','pagNum':'null', 'invertirWhereVista':'false'}
    headers = {'App' : '43', 'Content-Type' : 'application/json', 'Authorization': '77E8F0A2-27F8-4D80-A274-FB23409246C3'}
    response = requests.post(url, headers=headers, json=payload)
    
print(response.content)

