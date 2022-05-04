# Funções aninhadas
def executar_teste():
    def iniciar_teste():
        print('Inicializando teste...')
    
    def teste():
        print('Executando teste...')

    def finalizar_teste():
        print('Salvando resultado...')
        # salva resultado em disco

    iniciar_teste()
    teste()
    finalizar_teste()

executar_teste()
# iniciar_teste() # gera uma exceção

print()

# Funções podem ser salvas em variáveis e passada como parâmetro
def executar(func, x, y):
    resultado = func(x, y)
    return resultado

def potencia(x, exp):
    return x ** exp

operacao = potencia # note que não usamos os parênteses
resultado = executar(operacao, 4, 2)
print('Resultado: ', resultado)
print()

# Funções podem ser retornadas dentro de outra função
def selecionar_operacao(operacao):
    def potencia(x, exp):
        return x ** exp

    def divisao(x, y):
        return x / y

    if operacao == 'potencia':
        return potencia # note que não usamos os parênteses
    elif operacao == 'divisao':
        return divisao
    else:
        raise NameError('Operação desconhecida')

operacao = selecionar_operacao('divisao')
resultado = operacao(5, 2)
print('Resultado: ', resultado)