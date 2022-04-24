# Loops com o "for"
nome_da_usuaria = "Cleide"
for item in ['Bom dia', 'Good morning', 'Bonjour', 'Buenos dias']:
    item += f' {nome_da_usuaria}!'
    print(item)
print()

# Para executar um for loop n vezes, podemos escrever todos os números em um for
print(f'For loop com lista:')
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i, end=" ")
print()

# É mais fácil usar o a função range para não ter que escrever número a número
n = 10
print(f'For loop com range({n}):')
for i in range(n):
    print(i, end=" ")
print()

print(f'For loop com range(1,{int(n/2)}):')
for i in range(1,int(n/2)):
    print(i, end=" ")
print()

print(f'For loop com range(1,{n},2):')
for i in range(1,n,2):
    print(i, end=" ")
print("\n\n")

# É possível usar a função range para inicializar uma lista
minha_lista = list(range(0, 10, 2))
print("minha_lista: " + str(minha_lista))
print()

# Para gerar índices em cada item de uma lsita, existe a função enumerate
print('índice | item')
print('------ | ----')
for i, item in enumerate(minha_lista):
    print(f'   {i}   |  {item}')
print()

# Podemos forçar a interrupção de um loop com a palavra chave break
print('Uso do break')
for i, item in enumerate(minha_lista):
    print(f'{i}: {item}')
    if i == 2:
        break
print()

# Podemos pular um item no loop com a palavra chave continue
print('Uso do continue')
for i, item in enumerate(minha_lista):
    if i == 0:
        continue
    print(f'{i}: {item}')
print()

# Loops com "while"
nomes = ['Fernanda', 'Marina', 'Laís', 'Débora', 'Sabrina']
while len(nomes):
    nome = nomes.pop()
    print(nome)

# O loop abaixo nunca terminaria
idades = [20, 50, 33, 18, 25]
#while len(idades):
#    print(idades)

# Podemos usar o break para forçar a interrupção em um determinado momento
# e o continue para pular algum item da lista
contador = 0
while len(idades):
    contador += 1
    if contador == 2:
        continue
    elif contador == 10:
        break
    print(f'{contador}: {idades}')
print()

# Loops também podem ser aninhados
grupo1 = ['Fernanda', 'Marina', 'Laís', 'Henrique', 'João']
grupo2 = ['Gustavo', 'Sarah', 'Daniel', 'Débora', 'Sabrina']
num_possiveis_duplas = 0

for pessoa1 in grupo1:
    for pessoa2 in grupo2:
        print(f'Dupla {num_possiveis_duplas}: {pessoa1} e {pessoa2}')
        num_possiveis_duplas += 1
print(f'Existem {num_possiveis_duplas} possiveis duplas entre pessoas dos grupos 1 e 2')