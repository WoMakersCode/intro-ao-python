# Lógica booleana
x = True
y = True

print('x = ' + str(x) + '; y = ' + str(y))
print(x or y)
print(x and y)
print(not x)
print(not y)

print()

x = True
y = False

print('x = ' + str(x) + '; y = ' + str(y))
print(x or y)
print(x and y)
print(not x)
print(not y)

print()

x = False
y = False

print('x = ' + str(x) + '; y = ' + str(y))
print(x or y)
print(x and y)
print(not x)
print(not y)

# Números e letras podem sem convertidos para booleans.
# Por padrão, quase todos os valores em python são verdadeiros quando convertidos para
# True. As exceções são a palavra-chave 'None', o número 0 e strings vazias.

a = 0
b = 1
c = 1.0
d = 780
print('a: ' + str(bool(a)))
print('b: ' + str(bool(b)))
print('c: ' + str(bool(c)))
print('d: ' + str(bool(d)))

frase = 'A Dori é muito boazinha'
print('frase: ' + str(bool(frase)))

vazio = ''
print('vazio: ' + str(bool(vazio)))

especial = None
print('especial: ' + str(bool(especial)))