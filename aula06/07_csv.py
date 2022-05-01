import csv

# A função csv.reader() retorna um objeto leitor de CSV.
# Podemos iterar no leitor, recebendo cada registro já no formato de lista
with open('exemplo2.csv', mode='r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    alunos = []
    linha = 0
    for registro in leitor_csv:
        # pula o cabeçalho
        if linha == 0:
            linha = -1
            continue

        aluno = {'nome': registro[0], 'ano_nascimento': int(registro[1]), 'casa': registro[2]}
        alunos.append(aluno)

print(alunos)
print('------------------------------------------')

# A biblioteca CSV também possui um leitor que converte o CSV
# diretamente para um dicionário, considerando que a primeira linha
# é o cabeçalho.
with open('exemplo2.csv', mode='r') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    alunos = []
    for registro in leitor_csv:
        alunos.append(registro)

print(alunos)