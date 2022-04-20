# Comparar por igualdade
nome1 = "DoRi"
nome2 = "dOrI"

print('Igualdade: ', nome1 == nome2)
print('Igualdade: ', nome1.upper() == nome2.upper())
print()

# Comparar por diferença (ou "não-igualdade")
print('Não-igualdade: ', nome1 != nome2)
print('Não-Igualdade: ', nome1.upper() != nome2.upper())
print()

# Comparação de maior e maior ou igual entre números
print('maior que: ', 10 > 2)
print('maior que: ', 2 > 10)
print('maior que: ', 2 > 2)
print('maior ou igual que: ', 2 >= 2)
print('maior ou igual que: ', 2 > 1)
print()

# Comparação de strings
# Letras maiúsculas e minúsculas são consideradas diferentes umas das outras
print('apple == Apple? ', "apple" == "Apple")

# "apple" é inferior a (deve vir antes) à "banana", afinal, no dicionário palavras que começam com "a" vem antes de "b" (alfabeto)
print('apple < banana? ', "apple" < "banana")

# O valor inteiro correspondente de "A" é 65 e de "a" é 97. Portanto, "Apple" é menor do que "apple"
print('apple < Apple? ', "apple" < "Apple")

# Para descobrir o valor inteiro correspondente a um caractere, existe a função "ord()"
print('ord("A"): ', str(ord("A")))
print('ord("a"): ', str(ord("a")))
print('ord(" "): ', str(ord(" ")))

# Para descobrir a qual caractere da tabela ASCII de um inteiro, existe a função "chr()"
print('chr(65): ', str(chr(65)))
print('chr(97): ', str(chr(97)))
print('chr(32): ', str(chr(32)))
print()

# Precedência de operadores
# Python sempre usará os operadores aritméticos primeiro (exponenciação primeiro, depois multiplicação/divisão e depois adição/subtração). 
# Depois vêm os operadores de comparação relacionais (`==,!=,<=,>=,>,<`). 
# Finalmente, os operadores lógicos vêm por último (`and, or, not`).
x = 3
y = 6
# Na expressão abaixo as operações aritméticas são feitas primeiro, depois as comparações. 
# Depois, a prioridade é do "and" e o "or" será deixado por último.
resultado = x**2*5 >= 10 or y-6 <= 20 and 0
# Execução: ((x**2)*5) => 45
# Execução: (45) >= 10 => True
# Execução: (y-6) => 0
# Execução: 0 <= 20 => True
# Execução: True and 0 => True and False => False
# Execução: True or False => True
print('Resultado da expressão com precedência de operadores: ', resultado)
print()

# Função identidade "id()" retorna um valor inteiro que é garantido ser um identificador 
# único para um objeto durante todo seu ciclo de vida, ou seja, entre o começo e o fim 
# da execução do script pelo interpretador Python
print('id(nome1): ', id(nome1))
print('id(nome2): ', id(nome2))

nome3 = nome2
print('id(nome3): ', id(nome3))

# Se você criar uma nova string, ela vai ter um novo id
# Lembre-se de que strings são objetos imutáveis, e por isso toda
# nova string será um novo objeto, e por isso terá um novo id
nome3 = "dori"
print('id(nome3): ', id(nome3))

# O operador de comparação "is" testa se os objetos do lado esquerdo e 
# do lado direito do operador são o mesmo objeto, ou seja, se eles possuem o mesmo "id"
nome4 = nome3
print('id(nome4): ', id(nome4))
print('nome4 is nome3: ', nome4 is nome3)

# Da mesma forma, existe o operador "is not", que é a negação do operador "is"
print('nome4 is not nome3: ', nome4 is not nome3)
print()

# Qual a diferença entre o operador "is" e de comparação "=="?
# Se um objeto é o mesmo que outro (is), isso implica que os dois necessariamente iguais
# O oposto não precisa ser verdadeiro.
from datetime import time

hora1 = time(22,30)
hora2 = time(22,30)
print('hora1 == hora2: ', hora1 == hora2)
print('hora1 is hora2: ', hora1 is hora2)
print('hora1 is not hora2: ', hora1 is not hora2)
print('id(hora1): ', id(hora1))
print('id(hora2): ', id(hora2))

# O operador "in" testa se o valor existe em uma lista 
# ou em outros containers como tuplas e conjuntos.
# Veremos containers mais adiante neste curso.
nomes_de_gato_conhecidos = ["shiva", "princesa", "gaston", "mustafá"]
nome_buscado = input("Digite um nome de gato: ")
esta_na_lista = nome_buscado in nomes_de_gato_conhecidos
print(nome_buscado, 'está na lista? ', esta_na_lista)
