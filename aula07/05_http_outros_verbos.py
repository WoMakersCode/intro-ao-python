import requests
import json

# POST
URL = 'https://httpbin.org/post'
dados = {'username':'jacqueline', 'password':'12345'}
resposta = requests.post(URL, dados)
if int(resposta.status_code) == 200:
    conteudo = json.loads(resposta.text)
    print(conteudo)
print()

# PUT
URL = 'https://httpbin.org/put'
resposta = requests.put(URL, dados)
if int(resposta.status_code) == 200:
    conteudo = json.loads(resposta.text)
    print(conteudo)


# DELETE
URL = 'https://httpbin.org/delete'
resposta = requests.delete(URL)
if int(resposta.status_code) == 200:
    conteudo = json.loads(resposta.text)
    print(conteudo)