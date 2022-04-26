# List comprehensions - Compreensão de listas
palavras = ['a', 'de', 'mão', 'não', 'bola', 'carro', 'peteca']

resultado_loop = []
for palavra in palavras:
    if len(palavra) > 2:
        resultado_loop.append(palavra.upper())

print('Resultado do loop:', resultado_loop)

# A mesma lista pode ser criada através de uma compreensão de lista
resultado_compreensao = [palavra.upper() for palavra in palavras if len(palavra) > 2]
print('Resultado da compreensao de lista:', resultado_compreensao)
print()

# Strings podem ser "cortadas" em pedaços assim como listas, e podem ser usadas para inicializar listas com letras
dog = 'Doralice'
print(dog)
print('dog[2:5]:', dog[0:4])
print('dog[-5:]:', dog[-5:])
print()

dog_lista = list(dog)
print(dog_lista)
print('dog[2:5]:', dog_lista[0:4])
print('dog[-5:]:', dog_lista[-5:])
print()

# Podemos apagar um item de uma lista pelo index através da palavra-chave del
# A diferença do del para o lista.pop() é que o del não retorna nenhum valor.
# del também pode apagar o conteúdo de variáveis inteiras e pode ser usado com outras coleções.
del dog_lista[0]
print('del dog_lista[0]: ', dog_lista)
del dog_lista[0:2]
print('del dog_lista[0:2]: ', dog_lista)
del dog_lista
# print('del dog_lista: ', dog_lista) # gera uma exceção
print()

# Pilhas
pilha = [3, 4, 5]
pilha.append(6)
pilha.append(7)
print('pilha a:', pilha)
pilha.pop()
print('pilha b:', pilha)
pilha.pop()
print('pilha c:', pilha)
pilha.pop()
print('pilha d:', pilha)
print()

# Filas com list - ineficiente
fila_list = ["Érica", "Joana", "Miriam"]
print('fila_list a:', fila_list)
fila_list.append("Gláucia")
fila_list.append("Fernanda")
print('fila_list b:', fila_list)
fila_list.pop(0)
print('fila_list c:', fila_list)
fila_list.pop(0)
print('fila_list d:', fila_list)
print()

# Filas com deque - mais eficiente
from collections import deque
fila_deque = deque(["Érica", "Joana", "Miriam"])
print('fila a:', fila_deque)
fila_deque.append("Gláucia")
fila_deque.append("Fernanda")
print('fila b:', fila_deque)
fila_deque.popleft()
print('fila c:', fila_deque)
fila_deque.popleft()
print('fila d:', fila_deque)