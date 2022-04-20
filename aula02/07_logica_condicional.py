# Vamos conhecer mais sobre o nosso usuário perguntando
# se ele(a) gosta de café. Precisamos devolver uma mensagem diferente
# dependendo do que for a resposta.
resposta = input('   Você aceita um café? Digite sim ou não. ')
if resposta.lower() == "sim":
	fazer_cafe = True
	print("Ok!")
else:
	fazer_cafe = False
	print("Ok!")

print()

# Cuidado com a identação. Veja que o VSCode te ajuda a identificar os erros.
# if resposta.lower() == "sim":
# fazer_cafe = True
# print("Ok!")
# else:
#   fazer_cafe = False
#   print("Ok!")

# Note que o "print("Ok")" sempre será executado, indepentedente da opção.
# Por isso, ele pode ser removido do bloco identado e voltar para a lógica do
# bloco de código acima.
resposta = input('   Você aceita um café? Digite sim ou não. ')
if resposta.lower() == "sim":
	fazer_cafe = True
else:
	fazer_cafe = False
print("Ok!")

print()

# Outra forma de fazer ainda seria usar apenas o bloco "if".
fazer_cafe = False
resposta = input('   Você aceita um café? Digite sim ou não. ')
if resposta.lower() == "sim":
	fazer_cafe = True
print("Ok!")

# "elif" - testa outra condição na sequência
from datetime import datetime
print("Em qual estação do ano nós estamos?")
hoje = datetime.now()
inicio_outono = datetime(2022, 3, 20, 12, 33, 00)
inicio_inverno = datetime(2022, 6, 21, 6, 14, 00)
inicio_primavera = datetime(2022, 9, 21, 22, 4, 00)
inicio_verao = datetime(2022, 12, 21, 18, 48, 00)

if hoje.year == 2022 and hoje < inicio_outono or hoje >= inicio_verao:
	print('Verão')
elif hoje.year == 2022 and hoje >= inicio_outono and hoje < inicio_inverno:
	print('Outono')
elif hoje.year == 2022 and hoje >= inicio_inverno and hoje < inicio_primavera:
	print('Inverno')
elif hoje.year == 2022 and hoje >= inicio_primavera and hoje < inicio_verao:
	print('Primavera')
else:
	print('Erro: este programa só conhece as estações do ano 2022')
print()

# Poderíamos ter feito a mesma lógica com vários ifs.
# Note como a lógica abaixo é menos clara.
# Note como vários ifs 
print("Em qual estação do ano nós estamos?")
if hoje.year == 2022 and hoje < inicio_outono or hoje >= inicio_verao:
	print('Verão')
if hoje.year == 2022 and hoje >= inicio_outono and hoje < inicio_inverno:
	print('Outono')
if hoje.year == 2022 and hoje >= inicio_inverno and hoje < inicio_primavera:
	print('Inverno')
if hoje.year == 2022 and hoje >= inicio_primavera and hoje < inicio_verao:
	print('Primavera')
if hoje.year != 2022:
	print('Erro: este programa só conhece as estações do ano 2022')
print()

# Comparação aninhada - blocos de if/else dentro de outros blocos de if/else
# Note que o bloco de código dentro do primeiro `if` também precisa ser identado.
if hoje.year == 2022:
	if hoje < inicio_outono or hoje >= inicio_verao:
		print('Verão')
	elif hoje >= inicio_outono and hoje < inicio_inverno:
		print('Outono')
	elif hoje >= inicio_inverno and hoje < inicio_primavera:
		print('Inverno')
	elif hoje >= inicio_primavera and hoje < inicio_verao:
		print('Primavera')
else:
	print('Erro: este programa só conhece as estações do ano 2022')
print()

# Podemos usar os operadores que aprendemos para criar condições
from datetime import time

hora1 = time(22,30)
hora2 = time(22,30)

if hora1 is hora2:
	print('hora1 e hora2 são o mesmo objeto.')
elif hora1 == hora2:
	print('hora1 e hora2 não são o mesmo objeto, mas possuem valores iguais')
else:
	print('hora1 e hora2 não são o mesmo objeto e nem possuem valores iguais')