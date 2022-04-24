from datetime import datetime

# O código abaixo usa o módulo datetime para medir o tempo de processamento
# de um loop
print('----- Sem função -------')
inicio = datetime.now()
inicio_str = inicio.strftime('%H:%M:%S.%f')
print(f' > A tarefa começou em {inicio_str}')

number = 0
for i in range(100):
    number += 2
    print(number, end=" ")
print()

fim = datetime.now()
fim_str = fim.strftime('%H:%M:%S.%f')
print(f' > A tarefa terminou em {fim_str}')
print('\n\n')

# Note que no exemplo acima os blocos de código são quase idênticos.
# Esse é o caso em que faz mais sentido usar uma função.

# O código abaixo define uma função que imprime o horário de início
# ou fim de uma tarefa. Note que a variável "eh_inicio" vem dentro do 
# parênteses e é o que nós chamamos de parâmetro. Uma função pode ter ou não
# parâmetros, e eles são úteis para tornar as funções mais flexíveis.

def imprimir_tempo(eh_inicio): # def é a palavra chave usada para criar uma função em Python
    agora = datetime.now() # note que a função exige identação, assim como os blocos de código condicionais
    agora_str = agora.strftime('%H:%M:%S.%f')
    if eh_inicio == True:
        estado = 'começou'
    else:
        estado = 'terminou'
    print(f' > A tarefa {estado} em {agora_str}')

print('----- Com função -------')

imprimir_tempo(True)
number = 0
for i in range(100):
    number += 2
    print(number, end=" ")
print()
imprimir_tempo(False)
print()

print('----- Parâmetros -------')

# Parâmetros podem ser passados para uma função de duas maneiras:
# pela posição ou pelo nome
def minha_funcao(param1, param2, param3):
    print('param1: ', param1)
    print('param2: ', param2)
    print('param3: ', param3)

# Chamando a função e passando os parâmetros da maneira abaixo,
# o interpretador identifica cada parâmetro pela ordem. 
minha_funcao('Dori', 'Nina', 'Thor')
print()

# Outra forma de chamar a mesma função seria passando os parâmetros pelo nome.
# Como os parâmetros são identificados por nome, não há necessidade de se
# manter a ordem.
minha_funcao(param3 = 'Thor', param2 = 'Nina', param1='Dori')
print()

# Se deixarmos de passar algum dos parâmetros para a nossa função, vamos receber um erro
# porque por padrão, todos os parâmetros definidos na função são obrigatórios.
# minha_funcao(param3 = 'Thor', param2 = 'Nina')

# Podemos tornar os parâmetros opcionais para o nosso usuário.
# Para isso, só precisamos definir um valor padrão para o parâmetro caso
# nenhum seja definido explicitamente. Os parâmetros que tiverem valores
# padrão devem ser aparecer por último na definição da função.

def minha_funcao(param1, param2, param3='Thor'):
    print('param1: ', param1)
    print('param2: ', param2)
    print('param3: ', param3)

minha_funcao('Dori', 'Nina')
print()

# Ainda é possível definir outro valor para o último parâmetro.
minha_funcao('Dori', 'Nina', 'Paçoca')
print()

print('----- Retorno de valor -------')
# Funções podem executar algum tipo de processamento e retornar um valor
# como resultado desse processamento.
# No código abaixo, perceba que repetimos o mesmo padrão três vezes.

primeiro_nome = input('Digite seu primeiro nome: ')
inicial_do_primeiro_nome = primeiro_nome[0:1].upper()

nome_do_meio = input('Digite seu nome do meio: ')
inicial_do_nome_do_meio = nome_do_meio[0:1].upper()

ultimo_nome = input('Digite seu último nome: ')
inicial_do_ultimo_nome = ultimo_nome[0:1].upper()

print(f'As iniciais do seu nome são: {inicial_do_primeiro_nome}.{inicial_do_nome_do_meio}.{inicial_do_ultimo_nome}.')
print()

# Podemos reescrever este padrão que infere a inicial do nome do usuário
# utilizando uma função. Esta função vai precisar retornar como resultado a
# inicial, e para isso é utilizado a palavra chave "return"
def coletar_inicial_do_usuario(nome):
    inicial = nome[0:1].upper()
    return inicial

primeiro_nome = input('Digite seu primeiro nome: ')
inicial_do_primeiro_nome = coletar_inicial_do_usuario(primeiro_nome)

nome_do_meio = input('Digite seu nome do meio: ')
inicial_do_nome_do_meio = coletar_inicial_do_usuario(nome_do_meio)

ultimo_nome = input('Digite seu último nome: ')
inicial_do_ultimo_nome = coletar_inicial_do_usuario(ultimo_nome)

print(f'As iniciais do seu nome são: {inicial_do_primeiro_nome}.{inicial_do_nome_do_meio}.{inicial_do_ultimo_nome}.')
print()

# Podemos retornar valores diferentes dentro de uma mesma função.
# Note que depois que um valor é retornado, a execução da função termina
# e se houver mais algum código depois dissso no mesmo nível de identação,
# ele é ignorado pelo interpretador.
def gerar_mensagem_no_log(texto, nivel):
    if nivel.lower() == 'info':
        mensagem = f'Info: {texto}'
        return mensagem
    elif nivel.lower() == 'aviso':
        mensagem = f'Aviso: {texto}'
        return mensagem
    elif nivel.lower() == 'erro':
        mensagem = f'Erro: {texto}'
        return mensagem
    
    return 'Erro interno - nível desconhecido de mensagem'

mensagem_info = gerar_mensagem_no_log('Bem vinda!', 'info')
print(mensagem_info)
mensagem_aviso = gerar_mensagem_no_log('Já existe uma versão mais recente do aplicativo disponível. Atualize para não perder as novidades!', 'aviso')
print(mensagem_aviso)
mensagem_erro = gerar_mensagem_no_log('Usuário ou senha inválidos.', 'erro')
print(mensagem_erro)
mensagem_com_problema = gerar_mensagem_no_log('Oi Brasil.', 'outro')
print(mensagem_com_problema)
print()

# O tipo de retorno da função pode ser definido explicitamente em sua definição.
# Note que não foi necessário salvar o retorno da função em uma variável para
# imprimí-lo.
def contar_letras(palavra) -> int:
    numero_letras = len(palavra)
    return numero_letras
print('Número de letras: ', contar_letras('Dori'))

# 'comida' é uma variável é LOCAL porque só existe dentro do escopo da função "cardapio".
def cardapio():
    comida = 'hamburguer'
    print(comida)

# print(comida) # essa linha vai gerar um erro

# Variáveis declaradas fora de qualquer função são chamadas de GLOBAIS. Elas
# se encontram em um escopo que é acessível por qualquer função neste script.
bebida = 'refrigerante'
def cardapio():
    comida = 'hamburguer'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print()

# Ao alterar o valor de uma variável global dentro de uma função, na verdade é criada
# outra variável com o mesmo nome dentro do escopo da função e a variável global
# permanece intacta.
bebida = 'refrigerante'
def cardapio():
    comida = 'hamburguer'
    bebida = 'suco'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida)
print()

# Para alterar o valor de uma variável global dentro de uma função, precisamos informar
# a função que vamos utilizar a variável do escopo global.
bebida = 'refrigerante'
def cardapio():
    global bebida
    comida = 'hamburguer'
    bebida = 'suco'
    print('comida:', comida)
    print('bebida:', bebida)

cardapio()
print('bebida:', bebida)
print()
