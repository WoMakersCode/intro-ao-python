# Definicao da funcao principal
def main():
    miau(3)

def miau(n):
    for _ in range(n):
        print('miau')

# A funcao main deve ser chamada no final do arquivo
# main()

# A forma abaixo é a mais comum em livros e tutoriais:
if __name__ == "__main__":
    main()