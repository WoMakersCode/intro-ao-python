# Para identificar o tipo das variáveis, nós podemos usar a função type
frase = "Dori é fofinha"
print(type(frase))
idade_clarisse = 33
print(type(idade_clarisse))
idade_da_dori = 2.5
print(type(idade_da_dori))
python_eh_legal = True
print(type(python_eh_legal))

# O comando abaixo vai falhar porque estamos tentando concatenar
# variáveis de tipos diferentes
# > TypeError: can only concatenate str (not "float") to str
# print('A idade da Dori é ' + idade_da_dori)

# Para imprimir a mensagem, precisamos converter a idade_da_dori em uma string.
# Isso pode ser feito com a função str
print('A idade da Dori é ' + str(idade_da_dori))