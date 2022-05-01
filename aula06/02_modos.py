# Os modos r, w e a não permitem ler e escrever ao mesmo tempo
with open("numeros.txt", 'r') as arquivo: 
    arquivo.write('teste') # Exceção: io.UnsupportedOperation: not writable

# O modo r+ posiciona o cursor no **início** do arquivo e não apaga seu conteúdo.
# Se algo for escrito a partir dali, o conteúdo é sobrescrito.
with open('numeros.txt', 'r+') as arquivo:
    arquivo.write('Dori')

# O modo w+ posiciona o cursor no **início** do arquivo mas apaga seu conteúdo 
# antes de começar a leitura/escrita.
with open('numeros.txt', 'w+') as arquivo:
    arquivo.write('Dori')

# O modo a+ posiciona o cursor no **final** do arquivo sem apagar seu conteúdo.
with open('numeros.txt', 'a+') as arquivo:
    arquivo.write('Meg\nSarah')

# Modo binário - escrita
arquivo = open('teste.bin','wb')
teste = b'Python eh muito legal'
arquivo.write(b'Melhor linguagem de backend')
arquivo.close()

# Modo binário - leitura
arquivo = open('teste.bin','rb')
texto = arquivo.read()
print(texto)
arquivo.close()
print(texto.decode('ascii'))