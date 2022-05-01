from pathlib import Path

# Variável __file__ guarda o caminho para o arquivo atual
print(__file__)

# Podemos ver o caminho absoluto com o uso do módulo os (sistema operacional)
caminho_absoluto = Path(__file__).absolute()
print('caminho_absoluto:', caminho_absoluto)

# Podemos testar se um arquivo ou pasta existe
print(Path('./03_pastas.py').exists())
print(Path('minha_pasta').exists())

# A melhor forma de alterar caminhos é usando a classe Path do módulo pathlib
pasta = Path(caminho_absoluto).parent.parent
print('Pasta de cima: ', pasta.absolute())

# Se tentarmos escrever um arquivo em uma pasta que não existe, vamos
# ver uma exceção
# with open('minha_pasta/log.txt', 'w'):
#     print('texto') # FileNotFoundError: [Errno 2] No such file or directory: 'pasta/arquivo.txt'

# É uma boa prática testar se a pasta existe e só depois criá-la
minha_pasta = Path('minha_pasta')
minha_pasta.mkdir(exist_ok=True)
print(minha_pasta.exists())

caminho_log = minha_pasta.joinpath('log.txt')
print('caminho_log:', caminho_log)

with open(caminho_log, 'w') as arquivo:
    arquivo.write('Criou a pasta de log e o arquivo corretamente')