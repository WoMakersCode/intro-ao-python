# A função "input" permite que você peça ao usuário para gerar um dado de entrada.
# O valor inserido pelo usuário é salvo em uma variável
nome = input('Qual é o seu nome?')
print(nome)
print()

# Podemos melhorar a saída da interção acima acrescentando uma quebra de linha
# ao final da pergunta e imprimindo uma mensagem mais completa.
nome = input('Qual é o seu nome?\n')
print("Seu nome é: " + nome)