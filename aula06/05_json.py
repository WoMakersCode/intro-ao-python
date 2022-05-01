import json

# JSONs podem ser criados a partir de dicionários
personagem_dict = {'nome': 'Hermione', 'sobrenome': 'Granger'}
personagem_dict['casa'] = 'Grifinória'

# A função json.dumps() converte um dicionário para uma string no formato JSON
personagem_json = json.dumps(personagem_dict)
print('personagem_json:', personagem_json)
print()

# JSONs aceitam listas de itens como entrada
personagem_dict['qualidades'] = ['leal', 'inteligente', 'justa', 'leitora']
personagem_json = json.dumps(personagem_dict)
print('personagem_json 2:', personagem_json)
print()

# Podemos criar estruturas compostas de múltiplos itens em apenas um JSON
caracteristicas_fisicas = {'cabelo': 'castanho encaracolado', 'olhos': 'castanhos escuros'}
personagem_dict['caracteristicas_fisicas'] = caracteristicas_fisicas
personagem_json = json.dumps(personagem_dict)
print('personagem_json 3:', personagem_json)
print()

# Também é possível converter um JSON para o formato de dicionário em Python com a função json.loads()
personagem_json = """
{"nome": "Hermione", "sobrenome": "Granger", "casa": "Grifinória", "caracteristicas": ["leal", "inteligente", "justa", "leitora"], "caracteristicas_fisicas": {"cabelo": "castanho encaracolado", "olhos": "castanhos escuros"}}
"""
personagem_dict = json.loads(personagem_json)
print('personagem_dict:', personagem_dict)
print()

# O módulo JSON facilita a conversão de objetos JSON em dicionário e vice-versa através das
# funções json.dump() e json.load()
caminho = 'exemplo1.json'
with open(caminho, 'r') as arquivo:
    personagem_dict = json.load(arquivo)
    print(type(personagem_dict))
    print(f'personagem_dict lido do arquivo {caminho}:', personagem_dict)

with open(caminho, 'w') as arquivo:
    json.dump(personagem_dict, arquivo)

