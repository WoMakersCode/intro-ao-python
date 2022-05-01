# Aula 06 - Manipulação de Arquivos com Python, JSON, Decorators

## Manipulação de Arquivos com Python
* Até agora todas os dados que nós manipulamos nos nossos programas vieram de variáveis que foram criadas em tempos de execução e dados que foram escritos diretamente pelo usuário seja pela função `input` ou pela linha de comando.
* Os nossos programas também podem armazenar dados permanentemente e ler arquivos diretamente do computador.
* Arquivos são uma excelente forma de entrada e saída de dados para programas. Com eles, poderemos ler dados de outros programas e mesmo da internet.
* Um arquivo é uma área em disco (HD ou SSD) onde podemos ler e gravar informações.
  * Essa área é gerenciada pelo sistema operacional do computador, ou seja, não precisamos nos preocupar em como esse espaço é organizado em disco.
  * Do ponto de vista de programas, um arquivo é acessado pelo seu caminho no disco e é onde podemos ler e escrever linhas de texto ou dados em geral.
* Para acessar um arquivo, precisamos abri-lo. Durante a abertura, informamos o nome do arquivo, com o nome do diretório onde ele se encontra (se necessário) e que operações queremos realizar: leitura e/ou escrita. 
* Em Python, abrimos arquivos com a função `open()`
  * A função `open()` utiliza os parâmetros nome e modo. O nome é o nome do arquivo em si, por exemplo, leiame.txt. O modo indica as operações que vamos realizar.
  * A função `open()` retorna um objeto do tipo file (arquivo). É esse objeto que vamos utilizar para ler e escrever os dados no arquivo.

|Modo|                        Operações                 |
|----|--------------------------------------------------|
| r  |    Leitura                                       |
| w  |    Escrita (apaga o conteúdo que já existe)      |
| a  |    Escrita (adiciona ao conteúdo que já existe)  |
| b  |    Binário                                       |
| +  |    Atualização (leitura e escrita)               |

* Podemos trabalhar com arquivos de texto ou arquivos binários.
  * Arquivos de texto: Arquivos que podem ser lidos por humanos. Arquivos `.py`, `.txt`, `.json`, e `.html` são exemplos de arquivos de texto. Por padrão, cada linha do texto termina com o caractere `\n` (chamado de EOL - "end of line"). São maiores em tamanho do que um arquivo binário com o mesmo conteúdo.
  * Arquivos binários: Arquivos que só podem ser lidos por máquinas. Arquivos `.pdf`, `.bin`, `.pptx` e `.doc` são exemplos de arquivos binários. Não existe nenhuma forma padrão de terminar uma linha. São menores e do que arquivos de texto com o mesmo conteúdo, otimizados para serem lidos por máquinas.
* Ao trabalharmos com arquivos, devemos sempre realizar o seguinte ciclo: abertura, leitura e/ou escrita, fechamento.
  * Utilizamos o método `write()` para escrever ou gravar dados no arquivo, `read()` para ler e `close()` para fechá-lo.
  * A abertura realiza a ligação entre o programa e o espaço em disco, gerenciado pelo sistema operacional. As etapas de leitura e/ou escrita são as operações que desejamos realizar no programa, e o fechamento informa ao sistema operacional que não vamos mais trabalhar com o arquivo. 
  * O fechamento do arquivo é muito importante, pois cada arquivo aberto consome recursos do computador. Só o fechamento do arquivo garante a liberação desses recursos e preserva a integridade dos dados do arquivo.

### 01_ler_escrever_arquivos.py
**Lendo um Arquivo**
* Para ler um arquivo, usamos o modo `r` na função `open()`.
* A função `read()` lê todo o conteúdo do arquivo e retorna uma string
* A função `readline()` retorna a próxima linha de um arquivo com todo o seu texto, incluindo o `\n`
  * `readline()` pode aceita um parâmetro opcional que define o número de bytes a serem lidos.
  * Na prática, cada byte representa um caractere, então se passarmos um valor de 2 como parâmetro `readline(2)` significa que 2 caracteres serão lidos.
  * A cada chamada da função com o arquivo aberto, os próximos 2 caracteres disponíveis serão lidos.
* A função `readlines()` retorna uma lista de strings, onde cada linha do arquivo é retornada como uma string.

**Escrevendo em um Arquivo**
* Para escrever em um arquivo, usamos o modo `w` na função `open()`.
* A função `write()` escreve em um arquivo aberto. 
  * **Cuidado**! O conteúdo do arquivo é sempre apagado antes do `write()` começar a escrever.
  * A quebra de linha não é adicionada automaticamente.
* Também existe a função `writelines()` que recebe uma lista como entrada e escreve todas os itens da lista no arquivo aberto.
* Também podemos usar o modo `a` (_append_) para acrescentar mais conteúdo a um arquivo já existente.

**Usando o with**
* A palavra-chave `with` do Python que pode nos ajudar a não nos esquecermos de chamar as funções `close()` de nossos objetos.
  * A maior vantagem do `with` é que se algo inesperado acontecer dentro do bloco de código, como uma exceção, a estrutura `with` garante que o método close será chamado.
 
### 02_modos.py
* Podemos associar os modos `w`, `r`, e `a` com o `+` para conseguir ler e escrever em um arquivo ao mesmo tempo.
  * `r+` posiciona o cursor no **início** do arquivo e não apaga seu conteúdo. Se algo for escrito a partir dali, o conteúdo é sobrescrito.
  * `w+` posiciona o cursor no **início** do arquivo mas apaga seu conteúdo antes de começar a leitura/escrita.
  * `a+` posiciona o cursor no **final** do arquivo sem apagar seu conteúdo.
* Podemos criar, ler e escrever arquivos binários com o modo `b`.
  * Em geral, esse modo é usado por bibliotecas para escrever arquivos que vão ser lidos por algum programa específico. Por exemplo: modelos de Machine Learning geralmente são escritos em arquivos binários.
  * Para escrever um arquivo binário usamos o modo `wb`.
  * Não conseguimos escrever strings literais em um arquivo binário. Para converter as strings para o modo binário, acrescentamos o catactere `b` na frente da string.
    * Apenas caracteres ASCII são aceitos e strings binárias.
  * Para ler um arquivo binário usamos o modo `rb`.


### 03_pastas.py
* Quando a gente está escrevendo um programa e precisa persistir um arquivo, a gente precisa escolher onde esse arquivo vai ficar.
* Por padrão, os Python tenta ler e escrever arquivos na mesma pasta onde o programa está rodando.
* Como saber em qual pasta o programa está rodando?
  * No terminal: `dir` Windows ou `pwd` para Linux/MacOS
* Caminhos absolutos vs relativos
  * Caminhos absolutos: caminho completo no disco até o local do arquivo
    * Windows: `C:\Users\<usuario>\workspace\intro-ao-python\aula06\03_pastas.py`
    * Linux: `/Users/<usuario>/workspace/intro-ao-python/aula06/03_pastas.py`
  * Caminhos relativos: caminho parcial, relativo à pasta onde o interpretador está rodando. O exemplo abaixo considera rodar o interpretador Python na pasta raiz do repositório:
    * Windows: `aula06\03_pastas.py`
    * Linux: `aula06/03_pastas.py`
* A classe `Path` do módulo biblioteca `pathlib` provê diversas funções para permitir a manipulação de pastas no sistema operacional.
* Windows e Linux possuem separadores de caminho diferentes: `\` e `/`.
  * Para que um programa consiga ler e escrever caminhos corretamente no Windows ou Linux, o ideal é usarmos a função `joinpath()` para que o separador correto seja incluído.

### 04_desafio_11.py
Resolva o desafio proposto no [arquivo do desafio](./04_desafio_11.py)

## Arquivos JSON

### exemplo1.json
* JSON (ou _JavaScript Object Notation_) é um formato de arquivo muito comum para enviar e receber dados pela web, entre o servidores de backend e frontend.
* O Python possui um módulo chamado `json` que facilita muito a manipulação desses arquivos.
* Vantages do formato JSON:
  * Os dados são escritos de uma forma estruturada, que pode ser lida facilmente por um código.
  * É mais leve e mais simples que o seu antecessor XML.
  * É fácil de ser lido e escrito por humanos.
  * É agnostico em relação a linguagem de programação. Programas escritos em qualquer linguagem podem ler e escrever no formato JSP
* A sintaxe de JSON é muito semelhante aos dicionários de Python, já que os dados são escritos em pares de chave e valor.
  * Os dados são separados por vírgula.
  * JSON aceita guardar dados na forma de valores numéricos, strings, arrays (listas em Python) e booleans.
```json
{"nome": "Hermione", "sobrenome": "Granger", "língua": "inglês", "características": ["leal", "inteligente", "justa", "leitora"]}
```
* Algumas ferramentas possuem uma funcionalidade de formatação de JSON automaticamente para tornar o conteúdo mais legível.
  * O VSCode permite a formação de JSON em arquivos com a extensão `.json`
  * Outras ferramentas:
    - [JSONLint](https://jsonlint.com/)
    - [ConvertJson.com](http://www.convertjson.com/jsonlint.htm)
    - [JSON schema linter](https://www.json-schema-linter.com/)
  * **ATENÇÃO**: Cuidado com o uso de ferramentas online: você pode estar enviando dados sensíveis para serem processados por uma ferramenta 3a. 

### 05_json.py
* JSON podem ser criados a partir de Python `dict`s
* A função `json.dumps()` transforma um dicionário em python em uma string com o formato JSON
* JSON aceitam listas como itens de entrada e podem ser compostos de múltiplos dicionários internamente.
* A função `json.loads()` converte uma JSON string para o formato de Python `dict`.
* As funções `json.dump()` e `json.load()` são análogas às discutidas anteriormente, mas específicas para lidar com arquivos.

## Arquivos CSV
### exemplo2.csv
* Outro formato de entrada de dados muito comum é o formato CSV (_Comma Separated Value_).
* CSVs são comumente lidos por programas de planilhas (ex: Excel, Google Sheets, etc) e funcionam bem para armazenar valores como tabelas.
* Cada linha do arquivo é um registro diferente.
* Cada registro contém um ou mais campos, separados por vírgulas.
* Esse arquivo mostra o banco de dados de alunos de Hogwarts, contendo o nome dos alunos, o ano de nascimento e a casa a qual eles pertencem.
```csv
Cedric Diggory, 1977, Lufa-Lufa
Hermione Jean Granger, 1979, Grifinória
Draco Lucius Malfoy, 1980, Sonserina
Luna Lovegood, 1981, Corvinal
```

### 07_csv.py
* Python possui o módulo `csv` para facilitar o trabalho com arquivos desse tipo.
* A função `csv.reader()` retorna um objeto leitor de CSV, que é iterável.
* Cada item dentro do objeto leitor vai ser uma lista que represente o registro correspondente da tabela. Essa lista vai ter o mesmo número de itens que o número de colunas da tabela de entrada.
* A biblioteca CSV também possui o leitor `csv.DictReader()`, que transforma o conteúdo da tabela em um dicionário.
  * As chaves do dicionário são referentes ao conteúdo da primeira linha do CSV, que é o cabeçalho.

## Desafio 12
Resolva o desafio proposto no [arquivo do desafio](./08_desafio_12.py)