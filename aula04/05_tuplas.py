# Tuplas são inicializadas com valores separados por vírgula e (opcionalmente) parênteses
tupla = (2, 3, 4, 5, 6)
print('tupla:', tupla)
tupla = 2, 3, 4, 5, 6
print('tupla:', tupla)
print()

# Elementos podem ser acessados por índices
print('tupla[0]:', tupla[0])
print('tupla[-1]:', tupla[-1])
print('tupla[-3:-1]:', tupla[-3:-1])
print()
# Tuplas são imutáveis
# tupla.append(7)
# tupla.pop()

# Objetos dentro de tuplas podem ser mutáveis
tupla_2 = (2, 3, 4, [5, 6], 8)
print('tupla_2[3]:', tupla_2[3])
tupla_2[3].append(7)
print('tupla_2:', tupla_2)
print()

# Tuplas vazias ou com um item só
tupla_vazia = ()
print('tupla_vazia:', tupla_vazia)
tupla_de_um_item = 'Forever alone',
print('tupla_de_um_item:', tupla_de_um_item)
print()

# É possível criar uma nova tupla concatenando ou multiplicando outras tuplas
tupla_concatenada = tupla + tupla_2
print('tupla_concatenada:', tupla_concatenada)
tupla_repetida = tupla * 3
print('tupla_repetida:', tupla_repetida)
print()

# Funcões para lidar com tuplas
print('tupla.count(2):', tupla.count(2))
print('len(tupla):', len(tupla))
print('tupla_repetida.count(2):', tupla_repetida.count(2))
print('len(tupla_repetida):', len(tupla_repetida))
print('max(tupla_repetida):', max(tupla_repetida))
print('min(tupla_repetida):', min(tupla_repetida))
print()

# Desempacotamento de tuplas
tupla = ('Dori', 'Marrie', 'Caló')
dog, cat, bird = tupla
print(f'{dog}, {cat}, {bird}')
print()

# É possível usar o desempacotamento de tuplas para iterar sequências
sequencias = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for a, b, c in sequencias:
    print(f'a: {a}, b: {b}, c: {c}')
print()

# Outro uso comum é o retorno de múltiplos valores em uma função
def processar(dados):
    nome = dados[0]
    idade = dados[1]
    cidade = dados[2]
    return nome, idade, cidade

dados = [('Mariana', 27, 'Belém'), ('Keyliana', 39, 'Manaus'), ('Alessandra', 17, 'Jundaí')]
for item in dados:
    nome, idade, cidade = processar(item)
    print(f'nome: {nome}, idade: {idade}, cidade: {cidade}')
print()

# É possível capturar apenas algumas variáveis de uma tupla com a sintaxe do *
for item in dados:
    nome, *outros_dados = processar(item)
    print(f'nome: {nome}, outros_dados: {outros_dados}')
print()

# A sintaxe de desempacotamento é muito usada para chamar funções passando vários parâmetros como posicionais
def imprimir_divas_do_pop(diva1, diva2):
    print('diva1: {}, diva2: {}'.format(diva1, diva2))

parametros = ('Britney', 'Madonna')
imprimir_divas_do_pop(*parametros)

# Também é comum vermos essa sintaxe de desempacotamento sendo usada
# com o símbolo underline *_ para indicar que os valores não interessam
# e estão sendo descartados
diva1, diva2, *_ = ('Britney', 'Madonna', 'Lady Gaga', 'Rihanna', 'Beyoncé')
imprimir_divas_do_pop(diva1, diva2)