# Aula 05 - Dicionários, Conjuntos, Técnicas de loops em containers, Fluxo de execução e Linha de Comando

## Dicionários
### 01_dicionarios.py
* Dicionários são provavelmente a estrutura de dados mais importante. Também são chamados de "_hash maps_".
  * É uma forma muito útil de associar uma coisa com outra
* `dict`s são coleções de tamanho flexível que guardam pares de chave e valor, onde chaves e valores são objetos Python.
* Para criar um dicionário, utilizamos a sintaxe de colchetes `{}` e dois-pontos `:` para separar chaves de valores.
* Dicionários também podem ser criados com a função `dict()`
```python
d1 = {} # dicionário vazio
d2 = dict() # dicionário vazio
```
* Os valores em dicionários são guardados como se estivessem em um mapa, onde as coordenadas são a chave.
  * Dicionários são otimizados para guardar e retonar valores de maneira "instantânea".
* Dicionários **não** são ordenados. Não há garantia de que, ao se iterar em um dicionário, as chaves vão aparecer na mesma ordem.
* Valores em dicionários podem ser de qualquer tipo e podem ser duplicados, enquanto chaves não podem ser repetidas e precisam ser imutáveis. 
```python
# dicionário com chaves string e valores de diferentes tipos
d1 = {'chave1': 1, 'chave2': 'valor', 'chave3': (4, 5, 6)}
# dicionário com chaves inteiras e valores string
d2 = {1: 'valor1', 2: 'valor2', 3: 'valor3'}
print(d1['chave1']) # 1
d1['chave4'] = 7
print(d1['chave4']) # 7
```
* Elementos em um dicionário podem ser acessados através da sintaxe `dicionario[chave]` ou através do método `get()`.
  * Ao contrário das listas, as chaves aqui não são usadas para acessar índices.
* Podemos usar a função nativa `len()` para saber o número de itens em um dicionário
* Para serem usados como chaves, objetos precisam ser _hashable_.
  * É possível testar se um objeto é _hashable_, podemos testar o objeto com a função `hash()`.
  * A função `hash()` retorna um valor inteiro. Este valor é sempre o mesmo para o mesmo objeto.
  * As chaves geralmente são dos tipos `int`, `float`, `string` ou `tuple` (desde que todos os objetos dentro da tupla sejam imutáveis também).
```python
hash('string')
# resultado: 5023931463650008331
hash((1, 2, (2, 3)))
# resultado: 1097636502276347782
hash((1, 2, [2, 3])) # falha porque listas não são imutáveis
# TypeError Traceback (most recent call last) <ipython-input-129-800cd14ba8be> in <module>()
# TypeError: unhashable type: 'list'
```
* Objetos podem ser inseridos ou atualizados em um dicionário diretamente com a chave e o operador de atribuição `d[chave] = valor` ou com o método `update()`
* Podemos colocar um dicionário como um valor dentro de outro dicionário, criando "dicionários aninhados".
* A palavra-chave `del` pode ser usada para apagar chaves dentro de um dicionário ou apagar o dicionário como um todo.
* O método `pop()` pode ser usado para remover um par de chave-valor do dicionário, retornando o valor para aquela chave.
* O método `clear()` remove todos os itens de um dicionário, deixando-o vazio.
* Os métodos `keys()` e `values()` retornam listas contendo todos as chaves e valores, respectivamente.
* É muito comum ter uma lógica que procura um valor em um dicionário e, caso não encontre, precisa retornar um valor padrão. É possível fazer isso com o método `dicionario.get(chave, valor_padrao)`.
* Existe uma funcionalidade semelhante a "_list comprehensions_" para dicionários: "_dict comprehensions_". É muito semelhante, mas ao invés de usar colchetes (`[]`), usamos chaves `{}` e dois-pontos `:` para inicializar um `dict`.
* Para iterar em dicionários, podemos usar a função `<dicionario>.items()` que retorna a chave e o valor em cada iteração do loop `for`
* Os métodos `<dicionario>.keys()` e `<dicionario>.values()` retornam respectivamente as listas de chaves e valores em um dicionário, e podemos iterar usando apenas essas listas.
* A função `zip` junta listas ou tuplas de mesmo tamanho para criar objetos de tipo semelhante aos dicionários.
* Para testar se uma chave existe ou não em um dicionário, podemos usar o operador `in`.

## Sets (Conjuntos)
### 02_sets.py
* _Sets_ (ou conjuntos) são coleções de elementos únicos, onde os elementos não mantém a ordem.
* Você pode pensar em sets como se fossem dicionários sem valor, apenas chaves.
* Assim como dicionários, sets **não** são ordenados. Não há garantia de que, ao se iterar em um set, as chaves vão aparecer na mesma ordem.
* Elementos em sets são **únicos**, ou seja, cada elemento só pode aparecer uma vez.
* A maior vantagem de se usar um set so invés de uma lista é que um set é otimizado para checar se elementos existem já existem dentro dele.
* Para criar um set, utilizamos a sintaxe de colchetes `{}` ou a função `set()`.
  * A diferença para a sintaxe de dicionário é que não usamos os dois-pontos.
```python
meu_set = set([1, 2, 3]) # set inicializado com lista
meu_set = {1, 2, 3} # set inicializado com sintaxe de chaves
```
* Para adicionar itens em um set, podemos usar a função `add()`. Essa função adiciona apenas um item por vez.
* A função `update()` permite adicionar mais de um elemento por vez no set.
* Assim como as chaves de um dicionário, os valores inseridos em um set precisam precisam ser imutáveis, logo precisam ser _hashble_ (ser passíveis de uso pela função `hash()`).
  * Listas não podem ser adicionadas como itens em um set porque são mutáveis.
  * Tuplas podem ser adicionadas como itens em um set porque são imutáveis (_hashable_).
  * Sets são containers e podem guardar itens de diferentes tipos, desde que os itens sejam _hashable_.
* Como sets não são ordenados, não podemos acessar os itens por índices. Para acessar os itens em um set, podemos iterar por todos os elementos ou perguntar ao set se um determinado item existe usando a palavra-chave `in`.
* Para remover itens de um set, podemos utilizar os métodos `remove()` ou `discard()`. `del` não pode ser usado para remover um item específico do set (porque não existem índices), apenas para apagar o set inteiro.
  * `remove()` pode lançar uma exceção do tipo `KeyError` se o elemento não existir no set.
  * `discard()` remove o elemento mas não lança nenhuma exceção se o objeto não existir no set.
* O método `clear()` remove todos os elementos de um set.
* Operações com sets
  * Sets possuem suporte para operações matemáticas como interseção (operador `&` ou função `intersection()`), união (operador `|` ou função `union()`) e diferença (operador `-` ou função `difference()`).
  * Também é possível testar se um set é um "subset" de outro (operador `<=` ou função `issubset()`) ou se é um "superset" de outro (operador `>=` ou função `issuperset()`).
* Existe uma funcionalidade semelhante a "_list comprehensions_" para sets: "_set comprehensions_". É muito semelhante, mas ao invés de usar colchetes (`[]`), usamos chaves `{}` para inicializar um `set`.
* A lista completa das operações que podem ser realizadas com sets pode ser encontrada na [documentação oficial](https://docs.python.org/pt-br/3/library/stdtypes.html#set-types-set-frozenset).

## Desafio 9
Resolva o desafio proposto no [arquivo do desafio](./03_desafio_9.py)

## Fluxo de Execução e Função Main
### 04_fluxo_de_execucao/miau_1.py
* O interpretador executa um script python linha a linha.
  * Por mais esperto que o interpretador Python seja, ele assume que o código é escrito da esquerda para direita e de cima para baixo.
  * Se o interpretador ainda não viu a definição de uma função ou de uma variável, ele não vai reconhecê-las.
* Podemos apenas inverter o `for` e o `def` mas isso não é considerado uma boa prática.
  * Atrapalha a legibilidade do código - o leitor tem que ficar procurando visualmente onde estão as definições.

### 04_fluxo_de_execucao/miau_2.py
* A forma mais bacana de resolver isso é ter uma função principal no seu programa, que é normalmente chamada de `main()` (em várias linguagens).
* Nós definimos a lógica principal do nosso programa an função `main()`
* É uma boa prática ter um ponto de entrada para a lógica principal do nosso programa.
* Por convenção, a função `main()` deve ser sempre chamada no final do script.
  * Quando o interpretador chega lá, todas as funções e variáveis do módulo já foram definidas.
* Podemos chamar direto a função ou usar uma outra forma que é muito comum em livros e tutoriais:
```python
if __name__ == "__main__":
    main()
```

### 04_fluxo_de_execucao/miau_3.py
* O Python possui algumas variáveis globais especiais que são definidas pelo interpretador durante o fluxo de execução do programa.
* Podemos usar o debugger do VSCode para ver o valor da variável especial `__name__`.
  * No módulo principal, a variável vai ter sempre o nome de `__main__`.
  * Em módulos importados, essa variável vai ter o nome do módulo.
* Pra que serve isso?
  * Porque você pode ter um programa mais elaborado com vários módulos importados de diferentes pacotes, e pode haver várias funções `main()` sendo chamadas.
  * O `main()` correto a ser chamado é aquele que vai ser definido no script principal do seu programa.
  * Para o programa identificar qual é o `main()` correto, ele usa a variável `__name__`, que só tem o valor de `__main__` no script principal chamado diretamente pelo interpretador Python.

## Linha de comando e argumentos
### 05_linha_de_comando.py
* Outra forma comum do nosso usuário passar um valor para o programa é através de argumentos em linha de comando.
* No terminal, o usuário pode digitar valores na frente do nome do script `.py` que podem ser acessados pelo nosso programa.
* A variável especial `argv` o módulo `sys` guarda os parâmetros que foram passados na linha de comando em uma lista quando chamamos o nosso programa.
  * A palavra `python` não aparece na lista `argv`.
  * O primeiro item é sempre o caminho do script `.py`.
  * A partir do segundo item, se ele existir, podemos acessar os argumentos que foram mandados pelo usuário na linha de comando.
```bash
python 05_linha_de_comando.py
python 05_linha_de_comando.py Clarisse
```
* Já que `argv` é uma lista, podemos imprimir todos os argumentos em um loop `for`.
  * Para ignorar o nome do programa no seu loop, é só pegar o pedaço que interessa a partir do índice 1.

## Desafio 10 - Menti
Acesse o desafio no link https://www.menti.com/ua5ixjkyas

# Desafios offline - Microsoft Learn
* Complete o módulo ["Gerenciar dados com dicionários do Python"](https://docs.microsoft.com/pt-br/learn/modules/python-dictionaries/).
* Não esqueça de adicionar o PDF que comprova que você completou este módulo [na pasta de selos](../selos_microsoft_learn/).