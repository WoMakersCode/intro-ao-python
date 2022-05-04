import requests

# HTTP GET
URL = "http://womakerscode.org/construdelas/"
resposta = requests.get(URL)
conteudo = resposta.text
print('Código da resposta:', resposta.status_code)
print('Tipo da resposta:', resposta.headers['Content-Type']) # text/html
print('Conteúdo:')
print(conteudo)
print('--------------------------------------------------')
print()

# https://openweathermap.org/current
# Current weather data - Dados sobre o clima agora em BH
import json

API_KEY = '94c569356d41b9959a732a81b1a13451'
lat = '-19.930461972153026'
lon = '-43.93843961014884' 
units = 'metric'
lang = 'pt_br'
params = {'lat': lat, 'lon': lon, 'appid': API_KEY, 'lang': lang, 'units': units}
URL = f"https://api.openweathermap.org/data/2.5/weather"
resposta = requests.get(URL, params)
print('Código da resposta:', resposta.status_code)
print('Tipo da resposta:', resposta.headers['Content-Type']) # application/json
conteudo = json.loads(resposta.text)
print(conteudo)
print()

# Acessando os dados da resposta no JSON
local = conteudo['name']
descricao = conteudo['weather'][0]['description']
temp = conteudo['main']['temp']
temp_min = conteudo['main']['temp_min']
temp_max = conteudo['main']['temp_max']
print(f'Em {local} está fazendo {temp}o Celsius, {descricao}')
print(f'Temperatura mínima: {temp_min}')
print(f'Temperatura máxima: {temp_max}')

