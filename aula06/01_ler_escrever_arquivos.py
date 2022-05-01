#  Abrindo um arquivo no modo de leitura
caminho1 = 'numeros.txt'
arquivo = open(caminho1,'r')

# A função read() lê todo o conteúdo do arquivo e retorna uma string
conteudo = arquivo.read()
print('read():')
print(conteudo)

# A função close() fecha o arquivo e devolve os recursos usados ao sistema operacional
arquivo.close()
print()

# Abrir um arquivo que não existe vai gerar uma exceção
# FileNotFoundError: [Errno 2] No such file or directory: 'nao_existe.txt'
# arquivo = open('nao_existe.txt', 'r')

# Podemos ler um arquivo de diferentes formas.
# Cada vez que a função readline() é chamada, ela retorna a próxima linha de um arquivo com todo o seu texto, incluindo o \n
# no fim da linha.
print('readline():')
arquivo = open(caminho1,'r')
linhas = []

for _ in range(3):
    linhas.append(arquivo.readline())

print(linhas)
arquivo.close()
print()

# Ele pode aceitar opcionalmente um valor inteiro como parâmetro e, neste caso, apenas n caracteres na linha são
# retornados. A cada vez que a função é chamada, ela continua a leitura de onde parou anteriormente
print('readline(2):')
arquivo = open(caminho1,'r')
linhas = []

for _ in range(3):
    linha = arquivo.readline(2)
    linhas.append(linha)

print(linhas)
arquivo.close()
print()

# readlines() retorna uma lista com todas as linhas do arquivo lido
print('readlines():')
arquivo = open(caminho1,'r')
linhas = arquivo.readlines()
print(str(linhas) + '\n')

for linha in linhas:
    print(linha, end='')
print()
arquivo.close()

# Criando e escrevendo em um arquivo com a função write()
caminho2 = 'teste.txt'
arquivo = open(caminho2,'w')
arquivo.write('Python é muito legal')
arquivo.write('Melhor linguagem de backend')
arquivo.close()

# A função writelines() escreve linhas em formato de lista
caminho3 = 'pagina.html'
arquivo = open(caminho3,'w')
pagina = ['<!DOCTYPE html>\n', '<html>\n', '<body>\n', '\n', '<h1>Título</h1>\n', '<p>parágrafo</p>\n', '\n', '</body>\n', '</html>\n']
arquivo.writelines(pagina)
arquivo.close()

# A função append() acrescenta mas conteudo em um arquivo existe
arquivo = open(caminho2,'a')
arquivo.write('\nAgora eu só vou querer programar em Python')
arquivo.close()

# O blovo with garante que o arquivo é fechado sem precisarmos
# chamar o método close.
# Mesmo que uma exceção aconteca, o close vai ser chamado e os
# recursos vão ser devolvidos ao sistema operacional
caminho4 = 'precos_sacolao.json'
with open(caminho4, 'r') as arquivo_precos: 
    import json
    valores = json.loads(arquivo_precos.read())
    print(valores)