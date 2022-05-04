import requests

API_KEY = '94c569356d41b9959a732a81b1a13451'
lat = '-19.930461972153026'
lon = '-43.93843961014884' 
units = 'metric'
lang = 'pt_br'

# https://openweathermap.org/current
# Não passamos o API_KEY
URL = "https://api.openweathermap.org/data/2.5/weather"
params = {'lat': lat, 'lon': lon, 'lang': lang, 'units': units}
resposta = requests.get(URL, params)
print('Código da resposta:', resposta.status_code) # 401: acesso não autorizado
print('Tipo da resposta:', resposta.headers['Content-Type']) # application/json
print(resposta.text)
print()

# Passamos o API_KEY, mas não mandamos um parâmetro obrigatório
params['appid'] = API_KEY
params.pop('lat')
resposta = requests.get(URL, params)
print('Código da resposta:', resposta.status_code) # 400: requisição inválida
print('Tipo da resposta:', resposta.headers['Content-Type']) # application/json
print(resposta.text)
print()

# https://globo.com/ -> usando uma página inválida dentro desse servidor
# Mandando uma requisição GET
URL = f"https://globo.com/naoexisto"
resposta = requests.get(URL)
print('Código da resposta:', resposta.status_code) # 404: não encontrado
print('Tipo da resposta:', resposta.headers['Content-Type']) # text/html
print()

# Mandando uma requisição PUT
URL = f"https://globo.com/naoexisto"
resposta = requests.put(URL)
print('Código da resposta:', resposta.status_code) # 405: método não permitido
print('Tipo da resposta:', resposta.headers['Content-Type']) # text/html
print()