# LISTAS

# Inicializando uma lista com 4 valores
cachorros = ['Dori', 'Mei', 'Boni', 'Diana']
print(cachorros)
print()

# Inicializando uma lista vazia e acrescentando valores
cachorros = []
# cachorros = list()
cachorros.append('Dori')
cachorros.append('Mei')
cachorros.append('Boni')
cachorros.append('Diana')
print()

# Acessando items com o operador []
print(cachorros[1]) # Mei
print(cachorros[0]) # Dori
print()

# Índices negativos pegam os valores de trás pra frente
print(cachorros[-1]) # Diana
print()

# Fatias de uma lista
# O primeiro índice é incluído e o segundo fica de fora
print(cachorros[0:2]) # retorna o pedaço com os índices 0 e 1
print()

# Se omitir um dos índices, todos os valores do começo ou do fim são incluídos
print(cachorros[:3]) # ['Dori', 'Mei', 'Boni']
print(cachorros[2:]) # ['Boni', 'Diana']
print(cachorros[:-1]) # ['Dori', 'Mei', 'Boni']
print()

# Funções para lidar com listas
numero_de_itens = len(cachorros)
print('Número de itens na lista: ', numero_de_itens)
cachorros.sort() # altera a lista inplace
print('Lista ordenada (ordem alfabética): ', cachorros)
cachorros.insert(1, "Cloe")
print('Lista depois do insert: ', cachorros)
cachorros.remove("Mei")
print('Lista depois do remove: ', cachorros)
nome_removido = cachorros.pop(3)
print('Item removido:', nome_removido,'; Lista depois do pop:', cachorros)
print()

# Listas aninhadas
gatos = ['Tobias', 'Amora', 'Safira', 'Romeu']
animais = [cachorros, gatos]
print(f'Listas aninhadas: {animais}')
print(f'animais[1]: {animais[1]}')
print(f'animais[1][2]: {animais[1][2]}')
print()

# ARRAYS
from array import array
numeros = array('i')
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(2)
print("numeros:", numeros)
print("numeros[1]:", numeros[1])

# Funções com arrays
numeros.insert(0, 10)
print("numeros depois do insert:", numeros)
print("tamanho do array:", len(numeros))
numeros2 = sorted(numeros) # retorna uma cópia do objeto ordenada
print("numeros2:", numeros2)
print("numeros depois do sort:", numeros)
numeros.remove(2)
print("numeros depois do remove:", numeros)
item = numeros.pop(3)
print("numeros depois do pop:", numeros)
