# Não se preocupe se você não conhecer a linha abaixo, vamos
# falar de módulos nas próximas aulas
from datetime import datetime, date, time, timedelta

# O tipo datetime oferece o método now para retornar o exato momento da chamada da função
agora = datetime.now()
print('Agora: ' + str(agora))

# Note que a data é impressa em um formato diferente do que utilizamos
# no Brasil. Para imprimir a data da forma que conhecemos, precisamos
# utilizar a função strftime para indicar para o interpretador qual o formato
# que esperamos
print('Agora: ' + agora.strftime('%d/%m/%Y %H:%M:%S'))

# O "objeto" com o tipo datetime permite o acesso direto a cada
# um dos itens dentro do tempo. 
print('Dia: ' + str(agora.day))
print('Mês: ' + str(agora.month))
print('Ano: ' + str(agora.year))
print('Hora: ' + str(agora.hour))
print('Minuto: ' + str(agora.minute))
print('Segundo: ' + str(agora.second))

# Também podemos inicializar um objeto de datetime para o dia e a hora que
# queremos. Note que o VSCode ajuda você a preencher os parâmetros da função
# que inicializa um datetime
aniversario_da_dori = datetime(2022, 2, 22, 8, 30, 55)
print('Aniversário da Dori: ' + aniversario_da_dori.strftime('%d/%m/%Y %H:%M:%S'))

# Assim como existe o datetime, também temos tipos separados
# para a hora e o dia. Podemos inicializar um objeto do tipo tempo
# a partir de um objeto do tipo datetime ou especificar os valores
# de nossa preferência
hora = agora.time()
print('Hora: ', str(hora))
print('Tipo de "agora": ', str(type(agora)))
print('Tipo da "hora": ', str(type(hora)))

# Também podemos formatar a hora usando a mesma sintaxe utilizada
# para o datetime
hora_de_dormir = time(22,30,00)
print('Hora: ' + hora_de_dormir.strftime('%H:%M:%S'))

# De forma semelhante, existe o tipo dia. Ele também pode ser inicializado a partir de
# um objeto datetime ou utilizando os valores especificamente
dia_do_aniversario_da_dori = aniversario_da_dori.date()
# dia_do_aniversario_da_dori = date(2020,2,22) -> poderia inicializar o objeto assim também
print('Dia do niver da Dodó: ' + dia_do_aniversario_da_dori.strftime('%d/%m/%y'))
print('Tipo da "dia_do_aniversario_da_dori": ', str(type(dia_do_aniversario_da_dori)))

# Podemos fazer contas com datas utilizando o tipo timedelta
hoje = datetime.now().date()
print('Hoje é: ' + hoje.strftime('%d/%m/%y'))

#You can use timedelta to add or remove days, or weeks to a date
um_dia = timedelta(days=1)
ontem = hoje - um_dia
print('Ontem foi: ' + ontem.strftime('%d/%m/%y'))

uma_semana = timedelta(weeks=1)
semana_passada = hoje - uma_semana
print('Há uma semana era: ' + semana_passada.strftime('%d/%m/%y'))

# Também podemos converter strings para objetos datetime com a função
# 'strptime'
aniversario_str = input('Digite seu aniversário (dd/mm/aaaa): ')
aniversario_datetime = datetime.strptime(aniversario_str, '%d/%m/%Y')
print('O seu aniversário é em: ' + str(aniversario_datetime))