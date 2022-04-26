# Erros de sintaxe sempre interrompem a execução do programa.
quantidade = 10000
print('quantidade:', quantidade)

# if(quantidade = 3000)
# print("Você tem 3000 dinheiros.")

# Exceções são lançadas por erros de lógica
# quantidade = quantidade / 0

# Tratamento de exceções
print('Tratamento de exceções - except genérico')
lista = [1, 2, 3]
try:
    print ("    Segundo elemento = {}".format(lista[1]))
    # A linha abaixo lança uma exceção porque a lista só tem 3 itens
    print ("    Quarto elemento  = {}".format(lista[3]))
except: # captura qualquer tipo de exceção levantada pelo código
    # A exceção é tratada aqui ao invés de finalizar o programa
    print ("    Ocorreu um erro.")

print('    O programa continuou')
print()

# Podemos capturar tipos específicos de except e tratar esses tipos de forma
# diferente

lista = [1, 2, 3]
divisor = 0
print('Tratamento de exceções - except específico')
try:
    print ("Segundo elemento = {}".format(lista[1]))
    # A linha abaixo lança uma exceção porque a lista só tem 3 itens
    # quantidade = lista[1]/divisor
except IndexError: # captura apenas exceção de acesso a índices inválidos
    print ("Ocorreu um erro.")

print('O programa continuou')
print()

# Também podemos usar as palavras-chave else e finally optionalmente.
print('Tratamento de exceções - else e finally')
lista = [1, 2, 3]
try:
    print ("Segundo elemento = {}".format(lista[1]))
    # A linha abaixo lança uma exceção porque a lista só tem 3 itens
    quantidade = lista[3]/divisor
except IndexError as e: # captura apenas exceção de acesso a índices inválidos
    print ("Ocorreu um erro de acesso a índice: ", e)
else:
    print('Else - Se não ocorrer exceção, esse bloco é executado')
finally:
    print('Finally - Executou com ou sem exceção')

# Podemos lançar nossas próprias exceções
from meu_modulo import imprimir_no_log

imprimir_no_log('teste', 'invalido')
# Traceback (most recent call last):
#   File "01_erros_excecoes.py", line 72, in <module>
#     imprimir_no_log('teste', 'invalido')
#   File "01_erros_excecoes.py", line 70, in imprimir_no_log
#     raise ValueError(colorama.Fore.RED + 'Erro interno - nível desconhecido de mensagem' + colorama.Style.RESET_ALL)
# ValueError: Erro interno - nível desconhecido de mensagem