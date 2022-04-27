# Sets podem ser criados com a função set ou com a sintaxe de colchetes
primeiro_set = set([1, 2, 3, 3])
print('primeiro set:', primeiro_set)
segundo_set = {2, 2, 4, 5, 4, 5}
print('segundo set:', segundo_set)
print()

# Adicionando elementos no set
primeiro_set.add(10)
print('primeiro set:', primeiro_set)
segundo_set.update([8, 7, 8])
segundo_set.update((3, 9, 10))
print('segundo set:', segundo_set)
print()

# Acesso a itens dentro do set
for i in primeiro_set:
    print(i, end=' ')
print()

print('4 in primeiro_set:', 4 in primeiro_set)

# Removendo itens do set
# primeiro_set.remove(4) 
primeiro_set.remove(10)
primeiro_set.discard(10)
print('primeiro set:', primeiro_set)
print()

# Apagando todos os elementos de um set
meu_set = set('Dori')
print('meu set:', meu_set)
meu_set.clear()
print('meu set:', meu_set)
del meu_set
# print('meu set:', meu_set)  NameError
print()

# Operações com set
print('primeiro set:', primeiro_set)
print('segundo set:', segundo_set)

intersecao = primeiro_set & segundo_set
print('Interseção:', intersecao)
intersecao = primeiro_set.intersection(segundo_set)
print('Interseção:', intersecao)
uniao = primeiro_set | segundo_set
print('União:', uniao)
uniao = primeiro_set.union(segundo_set)
print('União:', uniao)
diferenca = primeiro_set - segundo_set
print('Diferenca:', diferenca)
diferenca = segundo_set.difference(primeiro_set)
print('Diferenca:', diferenca)
print()
print('primeiro_set é subset do segundo_set?', primeiro_set.issubset(segundo_set))
print('diferenca é subset do segundo_set?', diferenca.issubset(segundo_set))
print('segundo_set é superset do diferenca?', segundo_set.issuperset(diferenca))
print()

# Set comprehension
meu_set = {i for i in range(10)}
print('meu set:', meu_set)