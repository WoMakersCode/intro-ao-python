from sys import argv

if len(argv) == 2:
    nome = argv[1]
    print("Oi", nome)
else:
    print('Oi mundo')

# Podemos imprimir todos os argumentos em um loop for
for arg in argv[1:]:
    print('argumento: ', arg)