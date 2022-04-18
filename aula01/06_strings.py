# Você pode guardar strings em variáveis
primeiro_nome = 'Clarisse'

# Essa variável poderá ser reutilizada no seu código em outros momentos
print(primeiro_nome)

# Você pode concatenar strings usando o operador +
sobrenome = 'Simões'
print(primeiro_nome + sobrenome)

# Se você quiser utilizar espaços no meio do texto, você precisa adicioná-los
# explicitamente
print('Oi ' + primeiro_nome + ' ' + sobrenome)

# Existem muitas funções que você pode usar com strings
frase = 'o nome da cachorrinha é Dori'

print(type(frase))

# Upper retorna a string toda com letras maiúsculas
frase_maiuscula = frase.upper()
print(frase_maiuscula)
print(frase.upper())

# lower retorna a string toda com letras minúsculas
print(frase.lower())

# Capitalize retorna a primeira letra maiúscula e o resto minúsculas.
print(frase.capitalize())

# Count conta quantas vezes a letra apareceu na frase
print(frase.count('a'))

# Formatação de strings
nome_doguinha = 'Dori'
idade_doguinha = 2.5
concatenacao = 'A ' + nome_doguinha + ' tem ' + str(idade_doguinha) + ' anos de idade'
print(concatenacao)
funcao_format = 'A {} tem {} anos de idade'.format(nome_doguinha, str(idade_doguinha))
print(funcao_format)
interpolacao_de_variaveis = f'A {nome_doguinha} tem {str(idade_doguinha)} anos de idade'
print(interpolacao_de_variaveis)
print('A', nome_doguinha, 'tem', str(idade_doguinha), 'anos de idade')
print()

# Para saber o tamanho de uma string podemos usar o método nativo len()
print(f'Tamanho da string na variável "nome_doguinha": {len(nome_doguinha)}')
print(f'Tamanho da string "ConstruDelas": {len("ConstruDelas")}')