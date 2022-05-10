# ConstruDelas - Introdução ao Python
### Nome: 

## Visão Geral
Bem vinda ao repositório do curso ConstruDelas, módulo de Introdução ao Python.

Aqui vamos manter os exemplos utilizados durante as aulas.

Você poderá rodar os exemplos em sua própria máquina após ter seguido a configuração de ambiente proposta em aula.

Além disso, ao realizar um `fork` do nosso repositório para a sua própria conta no GitHub, você poderá publicar suas soluções para os exercícios propostos.

## Como utilizar este repositório
Você deverá realizar um _fork_ desse repositório para sua conta no GitHub e utilizar sua própria versão do repositório para trabalhar.

![Como fazer um fork do repositório](imagens/fork.png "Como fazer um fork do repositório")

O próximo passo é clonar o seu repositório em seu computador.
Após criar sua própria versão "forkada" do repositório original, vá até sua página de github e abra seu novo repositório.

Clique no botão "Code" e em seguida, no botão para copiar o endereço do seu repositório.

![Clique no botão de copiar (2) para copiar a URL do repositório](imagens/clone.png "Clonando o seu repositório para seu computador")

Para começar, abra uma ferramenta de terminal (PowerShell se você estiver utilizando Windows ou Terminal se estiver utilizando Linux ou Mac). Escolha uma pasta para onde seu repositório será clonado e utilize o comando `git` para clonar o repositório em seu computador.

``` bash
cd ~\workspace
git clone <endereço que você copiou>
```

Você poderá utilizar seu repositório de duas maneiras:

1. Rodar os códigos de exemplo realizados durante as aulas.
2. Resolver os desafios propostos e postar sua solução no seu GitHub pessoal.

Ao clonar o repositório, realize o primeiro `commit` incluindo seu nome neste arquivo README.

Bons estudos e divirta-se!

## Guia de Conteúdo

Cada aula possui:

1. Slides (dentro da pasta [slides](./slides))
2. Códigos de exemplo
3. Um arquivo README explicando o conteúdo dos códigos e dos slides dentro da pasta de cada aula
4. Desafios _online_ a serem realizados **dentro** do horário de aula.
5. Algumas aulas também possuem desafios _offline_ na plataforma [Microsoft Learn](https://docs.microsoft.com/pt-BR/learn/) a serem realizados **fora** do horário de aula.


|                 Módulo               | Aula |                        Tópicos                               |       Desafios para entrega        |
| ------------------------------------ | ---- | ------------------------------------------------------------ | ---------------------------------- |
| 1 - Lógica de Programação            |  1   | Interpretador Python, `print`, console, comentários, `input`, variáveis, tipos de dados, strings. | [Desafio 1](./aula01/04_desafio_1.py), [Desafio 2](./aula01/07_desafio_2.py), [Intro ao Python](https://docs.microsoft.com/pt-br/learn/modules/intro-to-python/), [Usar cadeias de caracteres no Python](https://docs.microsoft.com/pt-br/learn/modules/python-strings/) | 
| 1 - Lógica de Programação            |  2   | Dados numéricos, dados booleanos, dados de data e tempo, operadores aritméticos, operadores de comparação, funções nativas, lógica condicional |  [Desafio 3](./aula02/04_desafio_3.py), [Usar operações matemáticas no Python](https://docs.microsoft.com/pt-br/learn/modules/python-math-operators/), [Usar lógica Booliana em Python](https://docs.microsoft.com/pt-br/learn/modules/python-boolean-types/) | 
| 1 - Lógica de Programação            |  3   | Listas, arrays, estruturas de repetição (loops), funções, módulos, pacotes e _namespaces_ | [Desafio 5](./aula03/03_desafio_5.py), [Desafio 6](./aula03/06_desafio_6.py), [Usar loops "while" e "for" em Python](https://docs.microsoft.com/pt-br/learn/modules/python-loops/)|
| 1 - Lógica de Programação            |  4   | Erros e tratamento de exceções, debug, listas (parte 2), pilhas, filas e tuplas | [Desafio 7](./aula04/03_desafio_7.py), [Introdução às listas no Python](https://docs.microsoft.com/pt-br/learn/modules/intro-python-lists/) |
| 1 - Lógica de Programação            |  5   | Dicionários, sets (conjuntos), técnicas de loops em containers, fluxo de execução e parâmetros em linha de comando | [Desafio 9](./aula05/03_desafio_9.py), [Gerenciar Dados com Dicionários no Python](https://docs.microsoft.com/pt-br/learn/modules/python-dictionaries/) |
| 1 - Lógica de Programação            |  6   | Manipulação de arquivos, JSON, CSVs | [Desafio 11](./aula06/04_desafio_11.py), [Desafio 12](./aula06/08_desafio_12.py) | 
| 1 - Lógica de Programação            |  7   | Decorators e APIs | [Desafio 13](./aula07/03_desafio_13.py), [Desafio 14](./aula07/07_desafio_14.py), [Explorar o mundo das artes usando APIs RESTful](https://docs.microsoft.com/pt-br/learn/modules/use-apis-discover-museum-art/) |
| 2 - Programação Orientada a Objetos  |  8   | Orientação a objetos, classes, modelagem de um sistema real usando orientação a objetos | [Desafio 15](./aula08/02_desafio_15.py), [Introdução à programação orientada a objetos com Python](https://docs.microsoft.com/pt-br/learn/modules/python-object-oriented-programming/) |
| 2 - Programação Orientada a Objetos  |  9   | Construtores e destrutores, encapsulamento, propriedades, herança, herança múltipla (_mixins_) | - |
| 2 - Programação Orientada a Objetos  |  10  | Polimorfismo e classes abstratas | [Desafio 17](./aula10/03_desafio_17.py) |

## Referências
* [Microsoft Shows - Python for Beginners](https://docs.microsoft.com/pt-br/shows/intro-to-python-development/)
* [Microsoft Learn](https://docs.microsoft.com/pt-br/learn/)
* [Getting Started with Python - GitHub](https://github.com/microsoft/c9-python-getting-started)
* [Como pensar como um cientista da computação - IME/USP](https://panda.ime.usp.br/pensepy/static/pensepy/index.html)
* [Geek for Geeks - Python Programming Language](https://www.geeksforgeeks.org/python-programming-language/)
* [Python para Análise de Dados - Editora Novatec - Wes McKinney](https://leitura.com.br/python-para-analise-de-dados-L006-9788575226476)
* [CS50 2021 in Harvard - Lecture 6 - Python](https://youtu.be/ky-24RvI57s)
* [Introdução à Programação com Python - Editora Novatec - Nilo Ney Coutinho Menezes](https://www.amazon.com.br/Introdu%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o-com-Python-Algoritmos/dp/8575227181/)
* [Python Examples](https://pythonexamples.org/)