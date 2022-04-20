# Você pode utilizar variáveis para guardar o valor de números
pi = 3.14159
print('O tipo de ' + str(pi) + ' é ' + str(type(pi)))

# Números podem ser escritos em strings. Neste caso, o tipo é string e não int ou float
pi_str = '3.14159'
print('O tipo de ' + pi_str + ' é ' + str(type(pi_str)))
print()

# O interpretador precisa "adivinhar" o tipo da variável
# A função input sempre retorna uma string
primeiro_num = input('Insira um primeiro número ')
segundo_num = input('Insira um segundo número ')

# Como as variáveis "primeiro_num" e "segundo_num" são do tipo "str",
# o operador "+" concatena as strings ao invés de somar os valores.
print(primeiro_num + segundo_num)

# Para salvar os valores, precisamos converter as strings para tipos
# numéricos.
soma = int(primeiro_num) + int(segundo_num) + 1
print(soma)

soma_float = float(primeiro_num) + float(segundo_num) + 1.0
print(soma_float)

soma_mista = int(primeiro_num) + float(segundo_num) + 1
print(soma_mista)
print()

# O operador + pode adicionar dois números ou concatenar duas strings.
# Ele não sabe o que fazer se a operação envolver um número e uma string, 
# por isso gera um erro.
# > TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(28 + ' dias em fevereiro')
print()

# Você pode realizar uma infinidade de operações matemáticas com o python
primeiro_num = int(primeiro_num)
segundo_num = int(segundo_num)

print('Soma:')
print(primeiro_num + segundo_num)
print('\nSubtração:')
print(primeiro_num - segundo_num)
print('\nMultiplicação:')
print(primeiro_num * segundo_num)
print('\nDivisão:')
print(primeiro_num / segundo_num)
print ('\nExpoente:')
print(primeiro_num ** segundo_num)
print('\nDivisão arredondada:')
print(primeiro_num // segundo_num)