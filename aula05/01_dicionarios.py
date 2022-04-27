# Dicionários
d1 = {}
print('d1 vazio:', d1)
d2 = dict()
print('d2 vazio:', d2)
print()

# Dicionário com chaves de diferentes tipos
dict_chaves_inteiras = {1: 'Dori', 2: 'Mei', 3: 'Lua'}
print("Dicionário com chaves inteiras: ", dict_chaves_inteiras)
dict_chaves_strings = {'chave1': 1, 'chave2': 'valor', 'chave3': (4, 5, 6)}
print("Dicionário com chaves inteiras: ", dict_chaves_strings)
dict_chaves_mistas = {0: 1, 'chave2': 'valor', 'chave3': []}
print("Dicionário com chaves mistas: ", dict_chaves_strings)
print()

# Valores em dicionários podem ser duplicados, mas chaves são únicas únicas
contatinhos = {'Contatinho1': '11 98463-2843', 'Contatinho2': '11 97563-5937'}
print('Contatinhos:', contatinhos)
contatinhos['Contatinho3'] = '11 98463-2843' # insere um novo contatinho
print('Contatinhos:', contatinhos)
contatinhos['Contatinho1'] = '31 97583-0000' # atualiza o valor de 'Contatinho1'
print('Contatinhos:', contatinhos)
print()

# Elementos em um dicionário podem ser acessados pelo método get ou
# através de chaves
chave1 = 'Contatinho1'
print(chave1 + ': ' + contatinhos[chave1])
print(chave1 + ': ' + contatinhos.get(chave1))
print()

# Acessar chaves inexistentes gera uma exceção do tipo KeyError
# print('Contatinho4:', contatinhos['Contatinho4'])

# Podemos saber o número de itens em um dicionário com a função len()
print('Número de contatinhos: {}'.format(len(contatinhos)))
print()

# Chaves precisam ser hashable e imutáveis
chave2 = 'Contatinho1'
chave3 = 'Contatinho2'
hash1 = hash(chave1)
hash2 = hash(chave2)
hash3 = hash(chave3)
print('hash1:', hash1)
print('hash2:', hash2)
print('hash3:', hash3)

tupla1 = (1, 2, (3, 4))
hash4 = hash(tupla1)
print('hash4:', hash4)

tupla2 = (1, 2, [3, 4])
# hash5 = hash(tupla2) # TypeError: unhashable type: 'list'
print()

# Objetos em um dicionário podem ser atualizados com a sintaxe de chave ou com o
contatinhos['Contatinho2'] = '11 99998-9999'
contatinhos.update({'Contatinho5': '11 99998-9999'})
print('Contatinhos:', contatinhos)
print()

# Podemos pegar listas com todos os valores e chaves
print('Chaves:', contatinhos.keys())
print('Valores:', contatinhos.values())
print()

# Valores padrao
chave = 'outro'
print(f'Valor padrao de "{chave}": {contatinhos.get("outro", "tem não")}')
print()

# A palavra chave del e o método pop podem ser usados para remover itens de dicionarios
del contatinhos['Contatinho5']
tel_do_ex = contatinhos.pop('Contatinho1')
print('ex:', tel_do_ex)
print('Contatinhos:', contatinhos)

# Clear esvazia o dicionario
contatinhos.clear()
print('Contatinhos:', contatinhos)
del contatinhos
# print('Contatinhos:', contatinhos) # NameError: name 'contatinhos' is not defined
print()

# Compreensão de dicionários
chaves = ['Aline', 'Fernanda', 'Roberta', 'Sarah']
alunas = {nome: '' for nome in chaves}
print('alunas:', alunas)

# Iterando em dicionários
agenda = {'nome1': 'Rebeca', 'nome2': 'Martha', 'nome3': 'Lorena'}
for chave, valor in agenda.items():
    print(f'{chave}: {valor}')
print()

print('agenda.keys(): ', agenda.keys())
for chave in agenda.keys():
    print(f'{chave}')
print()

print('agenda.values(): ', agenda.values())
for valor in agenda.values():
    print(f'{valor}')
print()

# Criando dicionários a partir de listas
chaves = ['Batata', 'Feijão', 'Tomate']
valores = [8.00, 9.80, 10.00]

for chave, valor in zip(chaves, valores):
    print(f'{chave}: {valor}')
print()

# Testando se uma chave existe em um dicionário
sacolao = dict(zip(chaves, valores))
print('Batata existe no meu dicionário? ', 'Batata' in sacolao)
print('Arroz existe no meu dicionário? ', 'Arroz' in sacolao)