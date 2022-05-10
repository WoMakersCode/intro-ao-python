# Aula 09 - Construtores e Destrutores, Encapsulamento, Propriedades, Herança, Herança Múltipla

## Construtores e Destrutores
### 01_construtores.py
* Nós já vimos exemplos de métodos construtores na aula passada.
* Construtores são métodos especiais que são chamados durante a instanciação de um objeto.
* A função de um construstor é inicializar valores aos dados que são membros da classe quando uma instância é criada.
* O método `__init__()` é chamado construtor e é sempre chamado quando um objeto é criado.
* Se você não definir o método construtor explicitamente, o interpretador faz isso automaticamente por baixo dos panos, criando o **construtor padrão**.
* O construtor **construtor padrão** é o método `__init__(self)` que não aceita nenhum argumento além do `self`.
* O construtor também pode ser customizado para receber parâmetros. Neste caso, ele deixa de ser o construtor padrão e se torna um **construtor parametrizado**.
  * Ao declarar um construtor parametrizado, o interpretador python não cria mais outro construtor na classe.

### 02_destrutores.py
* Destrutores são métodos análogos aos construtores, só que para o objetivo oposto: eles são executados quando um objeto é destruído.
* A função de um destrutor é liberar a memória que o objeto estava usando quando ela não é mais necessária.
* Objetos desnecessários são excluídos automaticamente. Isso libera o espaço de memória conhecido como **coleta de lixo**.
* O nome de um método destrutor é `__del__(self)`.
* Assim como o construtor padrão, o destrutor é criado automaticamente pelo interpretador Python na classe e também é **chamado automaticamente**.
  * Isso tira do programador a responsabilidade sobre o gerenciamento direto da memória ocupada pelo programa.
* O destrutor é chamado quando todas as referências para o objeto são extintas ou quando a execução do programa é encerrada.
  * Quando um programa termina, o **coletor de lixo** do python destrói todos os objetos em memória. Esta é a última coisa que acontece durante a execução.
* Em geral, não é comum ver destrutores em códigos Python porque eles são executados automaticamente. Ainda assim é importante ter a noção de que eles existem, porque isso ajuda a entender melhor o que está acontecendo enquanto o seu programa está rodando.

## Encapsulamento - Slides
* Em Python, todas os atributos e métodos declarados em uma classe são públicos, ou seja, podem ser acessados pelo mundo externo.
* Isso não quer dizer que eles devam ser usadas por quem instancia um objeto daquela classe.
* Alguns atributos e métodos só existem na classe para seu funcionamento interno. Se forem alterados, podem gerar mal funcionamento e bugs no código.
* No exemplo abaixo, na classe `Quadrado` há dois atributos: `altura` e `largura`. Para que a classe de fato defina um quadrado, ela precisa ter altura e largura sempre iguais. Por isso, é interessante que quem usa a minha classe entenda que não deve mexer nesses atributos.
```python
class Quadrado:
  def __init__(self, medida):
    self.altura = medida
    self.largura = medida

  def area(self):
    return altura * largura

quadrado = Quadrado(2)
quadrado.altura = 3 # não é mais um quadrado
```
* Outro exemplo: na aula anterior, quando modelamos o funcionamento de um estacionamento, nossa classe tinha um método para buscar qual o `id` da próxima vaga livre para carros e motos. Esse método serve para auxiliar para a lógica interna da classe e também não gostaríamos que ele ficasse exposto.
* Para indicar ao usuário quais os atributos e métodos que ele não deve alterar na classe, nós utilizamos **convenções** nos em seus nomes.
* Existem duas convenções que são utilizadas em Python para se iniciar nomes de métodos e atributos:
  * **Protegidos**: Atributos e métodos que têm seus nomes iniciados com **_** (_underscore_) não devem ser acessados pelo mundo externo a não ser que o usuário saiba exatamente o que está fazendo, ou seja, ainda pode existir algum caso de uso em que faça sentido ter acesso a esse método/atributo. Em geral, o caso de uso mais comum para acesso a membros privados é com o uso de **herança**, que vamos ver a seguir.
  * **Privados**: Atributos e métodos que têm seus nomes iniciados com **__** (_underscore_ duplo) não devem ser acessados pelo mundo externo de forma nenhuma. Na prática, eles têm seus nomes alterados pelo interpretador Python mais ainda são públicos, e o que garante que eles não vão ser acessados é o bom senso do usuário da classe.
* Essas são o que nós chamaos de **regras de encapsulamento**, porque a ideia é encapsular atributos e métodos que são pertinentes a nossa classe mas não ao mundo externo.
* Em outras linguagens de programação que possuem orientação a objetos como C# e Java, temos palavras-chaves especiais para definir membros privados e protegidos, mas não em Python. Em Python nós utilizamos convenções nos nomes dos métodos.
* Se um usuário da classe quiser acessar os membros protegidos e privados, ele tem como fazer isso, mas vai estar quebrando as regras de encapsulamento, que de novo, são definidas por convenções nos nomes das variáveis.
* Existe uma forma de controlar um pouco melhor como um usuário vai acessar os atributos de uma classe, que é através de **propriedades**.
* Propriedades podem ser definidas pelo uso do _decorator_ `@property`. Esse decorator cria o método `getter` da propriedade.
* Para alterar o valor de uma propriedade externamente à classe, é preciso criar o método `setter`.

### 03_encapsulamento.py
* A classe `Pessoa` recebe três parâmetros: nome, profissão e identidade.
* O nome de uma pessoa não é algo que costuma mudar, mas pode ser que em algum caso especial seja necessário alterá-lo. Por exemplo: alguém que se divorcia e quer alterar seu sobrenome.
  * Podemos pensar na variável nome como sendo protegida, ou seja, mostramos ao usuário que não esperamos que esse variável seja alterada.
* Já a identidade é um dado sensível e não queremos que ele fique exposto de forma nenhuma. Por isso, podemos criá-lo como um dado privado.
  * Se tentarmos alterar um atributo privado, o seu valor não vai ser alterado.
* A profissão é algo que é relativamente comum de mudar, estão criamos ela como um atributo público.
* Nota: métodos especiais do Python começam e terminam com duplo _underline_. Isso não é o mesmo do que um método privado. Métodos privados possuem duplo _underline_ apenas no começo do nome.

### 04_propriedades.py
```python
class Quadrado:
  def __init__(self, medida):
    self.altura = medida
    self.largura = medida

  @property
  def altura(self):
    return self.__medida

  @altura.setter
  def altura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  @property
  def largura(self):
    return self.__medida

 @largura.setter
  def largura(self, valor):
    # executa algum tipo de validação
    self.__medida = valor

  def area(self):
    return self.largura * self.altura
```
* A classe `Quadrado` que vimos nos slides está definida aqui, com a adição de uma validação na hora de inicializar os valores das propriedades `altura` e `largura` e alguns prints para mostrar quando os métodos _getter_ e _setter_ de cada propriedade são chamados.
* Quando criamos o objeto `quadrado`, vemos que os _setters_ são chamados.
* Quando acessamos os valores, vemos que os _getters_ são chamados.
* Se removemos um dos _setters_, não conseguimos mais alterar o valor da propriedade diretamente.


## Desafio 16
* Acesso o desafio na plataforma Mentimeter através do [link](https://www.menti.com/h5qiom9yb7).

## Herança
* Slides

### 05_heranca.py
* A classe `Estudante` herda da classe `Pessoa`. A sintaxe para indicar isso é colocar o nome da "classe pai" dentro de um parênteses na frente do nome da "classe filha".
* Os métodos e variáveis da classe pai podem ser acessados com a função `super()`.
* É uma boa prática sempre chamar o construtor da classe pai no construtor da classe filha. É ele que garante que as propriedades da classe pai vão ser inicializadas corretamente.
* A classe `Estudante` herda os métodos e as propriedades públicas e protegidas da classe `Pessoa`.
* A classe `Estudante` pode sobrescrever os valores que foram herdados.
* Python provê funções nativas para testar se um objeto é instância de uma determinada classe, e se uma classe é derivada de outra.
* A classe `Trabalhador` também herda de `Pessoa`, e a classe `Professor` herda de trabalhador.
* `Professor` é um `Trabalhador` e também é uma `Pessoa`, portanto herda métodos e atributos de ambos.
* Atributos privados não podem ser alterados em classes filhas.
* Em Python, todas as classes herdam da classe `object`. Isso faz com que toda classe já comece com vários métodos e atributos.
* A função `dir()` mostra os atributos e métodos de um determinado objeto ou classe. Notem que as propriedades privadas aparecem aqui também, mas com nomes diferentes.

## Herança múltipla - Slide
* Em Python, uma classe pode herdar de mais de uma classe pai. Esse conceito é conhecido como herança múltipla.
* As vezes, classes que herdam de mais de uma classe são chamadas de **mixins**.
* Heraça múltipla é uma funcionalidade muito controversa, porque o uso dessa funcionalidade traz potencialmente muita complexidade para o código.
* Na maior parte das vezes onde alguém tenta resolver um problema com herança múltipla, existiriam soluções melhores e mais simples.
* O caso de uso mais legítimo é na criação de um _framework_.
* Ao trabalhar com Django, vocês podem ver casos onde uma classe vai herdar de duas ou mais classes.

### 06_heranca_multipla.py
* A classe `Logavel` define o método `logar`. Qualquer classe que herdar dela vai conseguir escrever uma mensagem no log e nós vamos saber de onde a mensagem está vindo pelo atributo `nome_da_classe` que é inicializado no construtor.
  * Ter uma classe assim é interessante porque a lógica de criar um arquivo de log, escrever as mensagens dentro dele e fechar o arquivo depois fica todo em um lugar só.
  * Quem está escrevendo um software não precisa se preocupar em escrever essa lógica toda vez, é só herdar de `Logavel`.
* A classe `Conexao` serve para conectar a um servidor de banco de dados.
  * O servidor costuma ser um endereço de IP com uma porta.
* A classe `MySqlDatabase` é uma classe de exemplo que se conecta ao banco de dados **MySql**, que herda tanto de conexão quanto de logável.
* O meu `framework` super chique aqui é só um metódo que recebe um objeto chamado `item` e testa se esse objeto é uma instância de cada uma das classes. Ele só chama os métodos pertinentes se for.