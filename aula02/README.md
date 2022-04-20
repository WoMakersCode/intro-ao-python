# Aula 02 - Continuação de Tipos, operadores, funções nativas e lógica condicional

## Variáveis numéricas
### 01_numeros.py
* Python tem dois tipos de variáveis numéricas: `int` (inteiros) e `float` (números com casas decimais)
* A função `input` sempre retorna uma string.
* Como as variáveis `primeiro_num` e "segundo_num" são do tipo `str`, o operador `+` concatena as strings ao invés de somar os valores.
* Para realizar uma soma, precisamos converter os valores lidos da string em números utilizando a função `int`.
* Também podemos converter os valores lidos para o tipo `float`
* Se a operação envolver um `float` e um `int`, o Python é esperto o suficiente para sempre mostrar o resultado com o tipo mais completo.
* O operador `+` pode adicionar dois números ou concatenar duas strings. Ele não sabe o que fazer se a operação envolver um número e uma string, por isso gera um erro. Você sabe como corrigir esse erro?
* É possível fazer contas utilizando valores numéricos.
* O operador de divisão arredondada `//` retorna como resultado apenas a parte inteira da divisão. Dessa forma, o resultado da divisão é sempre arredondado para baixo. Por exemplo:
  * `3.0 / 2 = 1.5` - aqui a parte inteira da resposta `1.5` é `1`. Logo, utilizando o operador `//` teremos `3.0 // 2 = 1`

## Tipos Booleanos
### 02_booleans.py
* Em Python a sintaxe de tipos booleanos utiliza letra maiúscula: `True` e `False`
* Operações com booleanos:

| Operação      |   Exemplo     |     Descrição     |
| ------------  | ------------- | ----------------- |
| `or`          | `x or y`      | `True` se qualquer um dos operandos for verdadeiro. `False` se ambos os operandos forem `False`. |
| `and`         | `x and y`     | `True` se ambos os operandos for verdadeiro. `False` se qualquer um dos operandos for `False`. |
| `not`         | `not x`       | Inverte o operando: `False` se x for `True` e vice-versa     |

* Números e letras podem sem convertidos para booleans com a função `bool`. Por padrão, quase todos os valores em python são verdadeiros quando convertidos para `True`. As exceções são a palavra-chave `None`, o número `0` e strings vazias.

## Tipos de data
### 03_tipos_de_data.py
* O módulo [datetime](https://docs.python.org/3/library/datetime.html) contém várias _classes_ que permitem a manipulação de dados que representam datas e horas.
  * Para este curso, você pode considerar que uma classe é equivalente a um tipo.
* As classes utilizadas para manipular data e hora são:
  * `date` que contém o ano, o mês e o dia
  * `time` que contém a hora, o minuto e o segundo
  * `datetime` contém dia e hora
  * `timedelta` representa uma duração de tempo entre dois `date`s, `time`s ou `datetime`s
* Para formatar a impressão de objetos de qualquer uma das classes acima, existe a função `strftime`. Através de algumas diretivas especiais, podemos mostrar ao interpretador como queremos que a data seja impressa. Por exemplo:
```python
print(datetime.now().strftime(%d/%m/%y))
```
`%d` representa o dia do mês como um número decimal com zeros a esquerda.
`%m` representa o mês como um número decimal com zeros a esquerda.
`%y` representa o ano sem século como um número decimal com zeros a esquerda.

* A lista completa de diretivas de formatação pode ser encontrada na [documentação oficial do Python](https://docs.python.org/pt-br/3/library/datetime.html#strftime-strptime-behavior)
  
## Desafio 3
Resolva o desafio proposto no [arquivo do desafio](./04_desafio_2.py)

## Operadores aritméticos e de atribuição
### 05_operadores_aritmeticos.py
* Operador de atribuição `=`: usado para inicializar variáveis. A variável deve vir do lado esquerdo da expressão, e o valor que ela vai ter fica do lado direito.
  * `1 = x` vai gerar um erro
  * Não confunda o operador de igualdade `=` com o operador de comparação para igualdade `==`.
* Operador de comparação para igualdade `==`: Testa se os operandos do lado esquerdo e direito são iguais.
* Operadores de adição e versão _in-place_: `+` e `+=`
* Operadores de subtração e versão _in-place_: `-` e `-=`
* Operadores de multiplicação e versão _in-place_: `*` e `*=`
* Operadores de divisão e versão _in-place_: `/` e `/=`
* Operadores de potenciação e versão _in-place_: `**` e `**=`
* Função `pow` é equivalente ao operador de potenciação
* Operadores de resto inteiro da divisão e versão _in-place_: `%` e `%=`
* Operadores de quociente inteiro da divisão e versão _in-place_: `//` e `//=`
* Função `divmod`: essa função retorna dois valores, que são o quociente inteiro e o resto inteiro da divisão
* Veja a tabela completa na [documentação oficial](https://docs.python.org/pt-br/3/library/stdtypes.html#numeric-types-int-float-complex)  do python

## Operadores de comparação, identidade e conversão de caracteres-inteiros
### 06_operadores_comparacao.py
* Comparação de igualdade `==`: testa se os objetos do lado esquerdo e direito do operador possuem o mesmo valor
* Comparação de diferença `!=`: testa se os objetos do lado esquerdo e direito do operador possuem valores diferentes
* Comparação de maior `>` e maior ou igual `>=`
* Comparação de menor `<` e menor ou igual `<=`
* Comparação de strings com `>`, `>=`, `<` e `<=`:
  * Isso porque em Python letras maiúsculas e minúsculas são consideradas diferentes umas das outras.
  * A forma como o computador sabe que eles são diferentes é que cada caractere corresponde a um valor inteiro único. Por exemplo, “A” é de 65, “B” é de 66, e “5” é 53. Esses números vêm da famosa [tabela ASCII](https://www.ime.usp.br/~pf/algoritmos/apend/ascii.html).
  * Você pode descobrir o chamado valor ordinal de um caractere utilizando a função `ord()`.
  * Há também uma função semelhante chamada `chr()` que converte inteiros para o seu caractere equivalente.
  * Tá, mas e daí? E daí que são esses valores que determinam a comparação.
  * As palavras são ordenadas em ordem **lexicográfica**. Isto é semelhante à ordem alfabética usada em um dicionário, exceto que todas as letras maiúsculas vêm antes de todas as letras minúsculas.
* Procedência de operadores
  * Python sempre usará os operadores aritméticos primeiro (exponenciação primeiro, depois multiplicação/divisão e depois adição/subtração). 
  * Depois vêm os operadores de comparação relacionais (`==,!=,<=,>=,>,<`). 
  * Finalmente, os operadores lógicos vêm por último (`and, or, not`).

| Nível de Prioridade   |             Categoria             |     Operadores    |
| --------------------  | --------------------------------- | ----------------- |
| 7 (alto)              |  potenciação                      | `**`              |
| 6                     |  multiplicação, divisão e módulo  | `*,/,//,%`        |
| 5                     |  adição e subtração               | `+, -`            |
| 4                     |  comparação relacional            | `==,!=,<=,>=,>,<` |
| 3                     |  lógico                           | `not`             |
| 2                     |  lógico                           | `and`             |
| 1 (baixo)             |  lógico                           | `or`              |

* Função identidade `id()`: retorna a “identidade” de um objeto. Ele é um inteiro, o qual é garantido que será único e constante para este objeto durante todo o seu ciclo de vida.
  * Dois objetos com ciclos de vida não sobrepostos podem ter o mesmo valor para `id()`.
  * Como saber que strings são únicas? Sempre que eu criar uma nova string, ela vai ter um novo id.
  * No interpretador CPython, o `id` de um objeto é seu endereço na memória
* `is` comparação de identidade: checa se os objetos do lado esquerdo e direito do operador são o mesmo objeto, isto é, se eles possuem o mesmo `id`.
  * Se um objeto é o mesmo que outro (`is`), isso implica que os dois necessariamente têm valores iguais.
  * Se dois objetos têm valores iguais, eles não precisam ser o mesmo objeto.
* `is not` negação da comparação de identidade: checa se os objetos do lado esquerdo e direito do operador **não** são o mesmo objeto, isto é, se eles não possuem o mesmo `id`.
* Operador `in`: testa se 
* Veja a tabela completa de operadores de comparação na [documentação oficial](https://docs.python.org/pt-br/3/library/stdtypes.html#comparisons) do Python.
* Podemos também "aninhar" mútiplas condições.

### Desafio 4 - Comparação de Strings - Mentimeter
Acesse o [link](https://www.menti.com/asz3dyb5ur) do desafio durante o horário da aula para participar.

## Funções nativas ou embutidas
* O interpretador do Python possui várias funções e tipos embutidos que sempre estão disponíveis.
* A lista completa da funções nativas pode ser encontrada na [documentação oficial do Python](https://docs.python.org/pt-br/3/library/functions.html#built-in-functions)
* Nós já usamos vários aqui:
  * `len()` - medir o tamanho de uma string
  * `int()` - operador de conversão para inteiro
  * `str()` - operador de conversão para string
  * `float()` - operador de conversão para o tipo float
  * `divmod()` - função que realiza a divisão e retorna o quociente e o resto inteiros

## Lógica Condicional
### 07_logica_condicional.py
* Até aqui nós vimos muitos conceitos básicos da linguagem, mas a gente ainda não construiu nada muito elaborado com ela. Agora é a hora onde a programação começa a ficar mais divertida.
* Na medida em que nossos programas vão ficando mais elaborados, a gente passa a precisar de dizer pro interpretador "Se isso acontecer, faça tal coisa, ou se não acontecer, faça aquela outra coisa".
* A gente precisa de ter uma forma de executar ações diferentes em cenários diferentes.
* Esse tipo de lógica pode ser completado usando as palavras chaves `if` e `else`:
```python
if expressao:
    # código
else:
    # outro código
```
* Se a expressão avaliada em `if` for `True`, o código dentro do bloco de `if` será executado. Caso contrário, o bloco dentro do código `else` vai ser executado.
* Na sintaxe acima, `expressao` deverá ser uma variável booleana ou uma expressão de comparação que retorne um `bool`. Note que depois da expressão do `if` e depois da palavra-chave `else`, precisamos adicionar o símbolo de dois pontos ":".
* Outro ponto importante é que para identificar qual bloco de código vai ser executado em cada caso, precisamos `identar` os blocos de código. 
  * `Identação` é basicamente colocar um número de caracteres de espaço no começo da linha para indicar ao interpretador que aquele código faz parte da lógica do `if` (ou do `else`).
  * Um espaço só não funciona como identação. Precisa ser um número específico de espaços, geralmente 2 ou 4. Isso é configurável pelo editor de código.
  * Cuidado para não usar o caracter "tab" (\t) para identar ao invés de 4 espaços. Visualmente eles são idênticos, para para o interpretador são coisas diferentes.
* Códigos adicionados depois do bloco de `if`/`else` com a identação comum voltam a fazer parte do fluxo normal de execução do programa.
* Também é possível usar apenas um `if` ao invés de `if` e `else` em alguns casos. 
  * O ideal é manter a legibilidade do código.
  * Código bom é código limpo, consistente e legível.
* Você também pode lidar com múltiplas condições de uma vez. Essa é a ideia da palavra chave  `elif`. Por exemplo, "Se A acontecer, faça tal coisa. Se A não acontecer mas B acontecer, faça outra coisa. Se nenhum deles acontecer, faça aquela outra coisa".
```python
if expressao:
    # código
elif outra_expressao:
    # outro código
elif outra_expressao:
    # outro código
else:
    # outro código
```
  * Usar o `elif` é mais elegante do que usar vários `if`s seguidos. Mas o `elif` só vai ser executado se a condição que vem anterior a ele falhar.
  * O `elif` faz sentido quando apenas uma das condições for ser verdadeira.
  * Quando usamos `elif`, não é obrigatório acrescentar o `else`, mas pode ser útil :) O `else` permite adicionar uma ação padrão para quando nenhuma das condições for verdadeira.
* O `if` é a forma mais importante de realizar uma avaliação de uma condição. A partir dele podemos criar lógicas com o `else` e o `elif`. Não é possível criar lógicas com `else` e  `elif` sozinhas, e isso nem faria sentido!
* Você pode utilizar os operadores de comparação para criar condições mais elaboradas.
  * Note que também precisamos identar o bloco de código interno.
  * Na prática, aninhar blocos em vários níveis dificulta a legibilidade do código. Por isso evite aninhar blocos de código em mais do que dois ou três níveis.
  * Lembre-se: código bom é código limpo, consistente e legível.
* Podemos usar os operadores que aprendemos para criar condições com `if`, `elif` e `else`.

# Desafios offline - Microsoft Learn
* Complete o módulo ["Usar operações matemáticas no Python"](https://docs.microsoft.com/pt-br/learn/modules/python-math-operators/).
* Complete o módulo ["Usar lógica Booliana em Python"](https://docs.microsoft.com/pt-br/learn/modules/python-boolean-types/).
* Não esqueça de adicionar os PDFs que comprovam que você completou estes módulos [na pasta de selos](../selos_microsoft_learn/).