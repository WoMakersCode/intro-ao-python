# Um Decorator permite adicionar qualquer comportamento antes ou depois de outra função.
def logger(func):
    def wrapper(x, y):
        print(f'Começando a função {func.__name__}')
        func(x, y)
        print(f'Terminando a função {func.__name__}')
    return wrapper

# A sintaxe de uso do decorator é o @nome_do_decorator
@logger
def potencia(x, exp):
    print(f'{x}^{exp} = {x ** exp}')

# Fluxo de execução principal
def main():
    potencia(5, 2)

if __name__ == '__main__':
    main()