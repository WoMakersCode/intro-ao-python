import conta_bancaria
import colorama

colorama.init()

print('Seu salário bruto é de {}'.format(conta_bancaria.salario_bruto))
valor_a_sacar = input('Quanto você deseja retirar da sua conta? ')
funcionou = sacar_na_conta(float(valor_a_sacar))

# Sacando novamente
valor_a_sacar = input('Quanto você deseja retirar da sua conta? ')
funcionou = sacar_na_conta(float(valor_a_sacar))

# Erros:
# 1. faltou colocar o namespace "conta_bancaria" para chamar a função "sacar na conta"
# 2. Linha 31 - a variável 'valor_na_conta' é local - não disse para a função que estava usando a variável global
# 3. Mesmo erro na funcao 'processar_salario'
# 4. expressao do 'recolher_imposto_de_renda'
# 5. if valor_na_conta <= valor: -> lógica invertida
# 6. Faltou atualizar a logica salario processado que está sendo repetida
