# Operador de atribuição inicializam o valor de uma variável
nome1 = "DORi"
nome2 = "DorI"
# "Dori" = nome1 vai gerar um erro

# O operador "=" é diferente do operador de "==".
# O operador "==" serve para comparar se dois valores são iguais.
# No caso do operador de compação, a ordem não importa
print(nome1 == nome2)
print(nome2.lower() == nome1.lower())

# Soma
a = 2 + 3 
print('a: ', a)
# Soma "in-place" - equivalente a "a = a + 1"
a += 1
print('a: ', a)
# Subtração
b = 5 - 2
print('b: ', b)
# Subtração "in-place" - equivalente a "b = b - 1"
b -= 1
print('b: ', b)
print()

# Divisão e Multiplicação
c = 6
d = 3
c = c / 2
d = d * 3
print('c: ', c)
print('d: ', d)

# Divisão e Multiplicação "in-place"
c = 6
d = 3
c /= 2 # equivalente a "c = c / 2"
d *= 3 # equivalente a "d = d * 3"
print('c: ', c)
print('d: ', d)
print()

# Potenciação
e = 5 ** 2
print('e: ', e)
f = 3
f **= 2 # equivalente a "f = f ** 2"
print('e: ', f)
# Potenciação com função "pow"
g = pow(4, 2) # equivalente a "e = 4 ** 2"
print('g: ', g)
print()

# Resto inteiro da divisão
resto = 5 % 2 # 5 / 2 = 4 resto 1
print('resto: ', str(resto))
resto = 5
resto %= 2
print('resto: ', str(resto)) # equivalente a "resto = resto % 2"
print()

# Quociente inteiro da divisão
quociente_inteiro = 10 // 3
print('quociente_inteiro: ', str(quociente_inteiro))
quociente_inteiro = 10
quociente_inteiro //= 3 # equivalente a "quociente_inteiro = quociente_inteiro // 3"
print('quociente_inteiro: ', str(quociente_inteiro))
print()

# Função "divmod": ssa função retorna dois valores, que são o quociente inteiro e o resto inteiro da divisão
quociente_inteiro, resto = divmod(10, 3) # 10 / 3 = 3 resto 1
print('quociente_inteiro: ', str(quociente_inteiro))
print('resto: ', str(resto))

# Divisão por 0
por_zero = 3 / 0

