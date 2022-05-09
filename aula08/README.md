# Módulo 2 - Aula 08 - Orientação a Objetos, Classes, Modelagem de um Sistema usando orientação a objetos

## O que é a orientação a objetos
### Slides
* Até o momento, nós vimos aqui a programação tradicional. Nela, programas são listas de instruções para o computador que definem dados (através de variáveis e tipos de dados) e trabalham com esses dados usando funções.
* Dados e funções são entidades diferentes, e que precisam ser combinadas para produzir o resultado esperado.
* Por causa dessa separação, muitas vezes a programação tradicional não nos dá uma forma muito intuitiva de representar a o mundo real.
* Isso faz com que a gente crie códigos como esse aqui.
```python
muda_canal_para_cima(televisao, canal) 
```
* A programação orientada a objetos é um **paradigma** de programação diferente dessa programação tradicional.
* Podemos pensar na programação orientada a objetos como uma forma de modelar os nossos programas como objetos. Ex: televisão é um objeto, livros, são objetos, mesas são objetos...
* Objetos tem dois componentes principais: **propriedades** e **comportamentos**.
  * Propriedades: cor, forma, pesa, tamanho, etc.
  * Comportamentos: são coisas que dá pra fazer com aquele objeto.
* Exemplo: considerando o objeto televisão:
  * Propriedades: se está ligada ou não, em qual canal está, quais são os canais máximo e mínimo que são permitidos na televisão, volume.
  * Comportamentos: mudar o canal pra cima e para baixo, ligar e desligar, aumentar e reduzir o volume.
* Na programação orientada a objeitos, as propriedades e os comportametos não ficam separados, eles ficam associados ao objeto. Isso leva a códigos desse estilo:
```python
televisao.mudar_canal_para_cima()
```
* Na programação orientada a objetos (POO), objetos não são _só_ variáveis (pedaços da memória que guardam valores). Eles também são representações de algo no mundo real (sujeito/ator), e reúnem propriedades e comportamentos desse sujeito.
* Objetos são auto-contidos e reutilizáveis:
```python
televisao.ligar()
televisao.aumentar_volume()
```
* Essa forma de modelar o mundo real cria códigos claros que mostram quem é o sujeito (**objeto**) e qual é o comportamento que está sendo invocado (**método**).
  * Métodos são funções associadas a uma classe e atuam sobre um objeto.
* POO não substitui a programação tradicional – ela te dá mais ferramentas para escrever um código limpo, conciso e legível.
* POO traz novos conceitos para a linguagem: classes, herança, encapsulamento, abstrações e polimorfismo.
* Como criar meus próprios objetos em Python? Utilizando classes.
* Classes estruturas usadas para definir um novo tipo de dados (criado pela programadora). Elas descrevem o que um objeto vai ser, mas elas não criam o objeto em si.

### 01_primeira_classe.py
* Classes são criadas com a palavra-chave `class`.
* Conveção para nomes de classes em Python: **PascalCasing**.
* Para instanciar um objeto de uma classe, adicionamos parênteses ao nome da classe. 
  * Uma classe pode ter várias instâncias, e cada uma delas é isolada da outra e tem seus próprios atributos e métodos.
  * Chamar um método em uma instância não altera a outra.
* Toda classe tem um método especial `__init__`, que é sempre chamado quando um novo objeto daquela classe é criado.
  * O método `__init__()` é chamado de **construtor** porque ele inicializa os valores padrão do objeto.
* O primeiro parâmetro dos métodos de uma classe é chamado de `self`. Ele representa a instância sobre a qual o método vai atuar.
  * `self` dá acesso a atributos e outros métodos daquela mesma instância.
  * Não é necessário passar o parâmetro `self` ao chamar os  métodos da classe porque o interpretador faz isso aumaticamente para nós.
  * Entretanto, não se esqueça de declarar `self` como o primeiro parâmetro de seus métodos.
* Quando chamamos o método `ligar()` em uma instância, estamos alterando o estado apenas dela. A outra televisão permanece desligada.
* Se tentamos imprimir o conteúdo do objeto, visualizamos uma representação estranha. O Python mostra o tipo do objeto e o endereço da memória em que aquele objeto foi guardado.
  * Quando imprimimos um objeto do tipo `Televisao`, o interpretador Python chama o método especial `__str__()` internamente e imprime o conteúdo retornado por esse método.
  * O método especial `__str__()` permite que nós criemos uma representação em `string` para uma instância que tenha o tipo definido pela nossa classe.
* Quando digitamos o nome da variável que contém o objeto no VSCode e incluímos o ponto final `.`, o VSCode mostra uma lista de opções de métodos e atributos relativos a nossa classe.
* No módulo `datetime` da biblioteca padrão, temos as classes `datetime`, `date` e `time`.
  * Passando o mouse em cima dos nomes no `import`, podemos ver que eles são classes.

## Desafio 15
Resolva o desafio proposto no [arquivo do desafio](./02_desafio_15.py)

### Modelagem OOP - Slides
* Todo software usa a mesma série de etapas para resolver problemas:
1. **Entrada de dados**: os dados são lidos de algum lugar, que pode ser o armazenamento de dados como um sistema de arquivos ou um banco de dados.
2. **Processamento**: os dados são interpretados e possivelmente alterados para serem preparados para exibição.
3. **Saída de dados**: os dados são apresentados para que um usuário físico ou um sistema possa lê-los e interagir com eles.
* A programação orientada a objetos cria **modelos** do mundo em que os dados são operados.
* Os modelos possuem classes que representam objetos ou atores do mundo real, e como eles interagem entre si.
* Durante a fase de modelagem, você examina uma descrição de um domínio e tenta analisar o texto sobre o que ocorre.
* A primeira etapa é identificar os **atores**. Eles são chamados de atores porque atuam no domínio e executam uma ação.
  * Por exemplo, uma impressora (ator) imprime (ação).
  * Atores serão objetos no nosso programa, geralmente são substantivos que representam do mundo real.
* Em seguida, você examina as descrições dos atores e de todos os **dados** necessários para executar a ação.
* Após identificar atores, você examina o que eles fazem, que é o **comportamento**.
* Os atores são transformados em objetos, as características são codificadas como dados nos objetos e os comportamentos são funções que também são adicionadas ao objeto.
* A ideia é que os dados nos objetos podem ser alterados chamando funções nos próprios objetos.
* Também há a noção de que os objetos interagem uns com os outros para chegar a um resultado tangível, gerando uma saída para o nosso programa.
* Modelagem trata-se de aprender a identificar os atores, os dados necessários e o tipo de interação que está ocorrendo.
* Você pode modelar um sistema investigando sua descrição, que é relacionada as **regras de negócio**.

### Modelagem de um estacionamento - slides
* Vamos fazer a modelagem de um sistema de estacionamento.
* Para isso, vamos levantar os requisitos.
* Então a gente conversa com um dono de estacionamento e ele nos explica o seguinte:
  * O estacionamento é um pátio de apenas um andar. Ele possui 50 vagas.
  * Há 5 vagas para carros e 5 vagas para motos. Vagas para carro são maiores do que as vagas para motos.
  * Carros e motos são identificados por suas placas.
  * Vagas são identificadas por um número. Cada vaga tem um número identificador único.
  * Carros só podem ser estacionado em vagas específicas para carros.
  * Motos preferencialmente são estacionadas em vagas de motos, mas se não houver mais vagas exclusivas de motos disponíveis, motos podem ser estacionadas em vagas de carros.
  * É preciso ter controle sobre qual carro está em qual vaga para agilizar a saída quando o dono vem buscar.
  * É preciso saber o número de vagas livres de carro e de moto para que o estacionamento saiba se pode novos carros e motos.
* O primeiro passo é identificar os atores, ou seja, os substantivos que vão se transformar em classes no nosso sistema.
  * Estacionamento, Carro, Moto e Vaga.
* Em seguida, identificamos os atributos de cada ator.
  * Estacionamento: vagas de carro, vagas de moto, carro_para_vaga, moto_para_vaga, total_de_vagas_livres_carro, total_de_vagas_livres_moto
  * Carro: placa
  * Moto: placa
  * Vaga: identificador, tipo
* Vamos então olhar identificar quem vao ser os dados de entrada, o processamento e a saída do nosso programa:
  * Em nosso sistema, a entrada vai ser um conjunto de carros (pode ser uma lista cheia de objetos dos tipos `Carro` e `Moto`, um dicionário, etc).
  * O processamento vai cuidar do estacionamento, sendo responsável por atualizar a entrada e saída de carros.
  * Ainda precisamos de algum tipo de controle para evitar que o mesmo objeto de carro o moto seja estacionado duas vezes dentro do estacionamento. Para isso, adicionamos um atributo `estacionado` nas classes `Carro` e `Moto` que será um valor booleano atualizado pelos métodos `estacionar()` e `sair_da_vaga()`.
  * Também precisamos de uma forma de mostrar qual é o estado atual do estacionamento, que é a nossa saída. Para isso, adicionamos o método `estado_do_estacionamento()` na classe `Estacionamento`.


### estacionamento.py
* Este módulo define as classes `Estacionamento`, `Carro`, `Moto` e `Vaga` que nós discutimos.
* As classes `Carro` e `Moto` são muito semelhantes.
* A classe `Vaga` recebe em seu construtor qual é o tipo daquela vaga, e possui métodos para realizar a sua ocupação e desocupação, salvando a placa do veículo que está ocupando a vaga no momento.
* A lógica mais interessante se concentra na classe `Estacionamento`:
  * O construtor inicializa os atributos que nós vimos anteriormente.
  * Utilizamos o método `inicializar_vagas` para preencher os dicionários `vagas_carro` e `vagas_motos` com objetos do tipo `Vaga`, onde cada chave é o identificador de vaga e cada valor é um objeto do tipo `Vaga`.
  * O primeiro `id` de vaga de moto é o próximo valor inteiro depois do  último `id` da vaga de carro.
  * O método `estacionar_carro()` busca a primeira vaga de carro livre na coleção de vagas de carro.
    * Se ele não encontra nenhuma vaga livre, uma exceção é lançada.
    * Se encontra, ele atualiza todas os atributos necessários para realizar o controle de ocupação da vaga.
    * O dicionário `carro_para_vaga` mantém um dicionário para agilizar a busca de em qual vaga o carro foi estacionado. 
  * O método `estacionar_moto()` funciona de forma semelhante, mas precisa levar em conta que motos podem ser estacionadas em vagas de carro caso todas as vagas de moto já estejam ocupadas.
  * O método auxiliar `buscar_id_da_proxima_vaga_livre()` inclui a lógica para buscar vagas de carro e de moto. É nele que incluímos a lógica que tenta buscar o identificador de vagas de moto e, em seguida, de carros caso não tenhamos vagas de moto livres.
  * Os métodos `remover_carro()` e `remover_moto()` encontram em qual vaga o veículo está estacionado e atualizam os valores de atributos pertinentes a remoção de veículo da vaga.
  * Finalmente, o estado do estacionamento é mostrado através de uma `string`.
  * Adicionamos o método especial `__str(self)__` para poder imprimir o estado do estacionamento com a função `print()`.


### 03_modelagem.py
* Agora vamos utilizar as classes que criamos para simular um sistema de estacionamento.
* Começamos incluindo todas as classes do módulo `estacionamento` no _namespace_  corrente, já que vamos utilizar todas elas.
* Criamos duas listas: uma de carros e uma de motos. Utilizamos a biblioteca `random` para gerar valores inteiros aleatórios que representem as placas dos veículos.
* Em seguida, testamos as lógicas que criamos.


# Desafios offline - Microsoft Learn
* Complete o módulo ["Introdução à programação orientada a objeto com o Python"](https://docs.microsoft.com/pt-br/learn/modules/python-object-oriented-programming/).
* Não esqueça de adicionar os PDFs que comprovam que você completou estes módulos [na pasta de selos](../selos_microsoft_learn/).