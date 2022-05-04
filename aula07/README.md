# Aula 07 - Decorators, APIs

## Decorators
### Slide
* _Decorators_ são formas de adicionar funcionalidades em blocos de código sem necessariamente alterá-los, deixando o código mais limpo e conciso.
* A sintaxe de uso de um _decorator_ é adicionar o nome do decorator com o caractere `@` antes do bloco de código a ser chamado.
```python
@logger
def funcao():
  # realiza operacao
```
* _Decorators_ permitem que adicionemos códigos que podem rodar antes e/ou depois de uma função.
  * No exemplo acima, o _decorator_ `@logger` poderia fazer com que o aplicativo escrevesse no log que vai executar a função. Também pode fazer com que o app imprima uma mensagem quando concluir a execução da função.
* Decoradores são frequentemente usados em `frameworks` como Flask e Django.
* A interação mais comum com _decorators_ para aplicações web é usar, não criar. Ainda assim é interessante entender como eles funcionam por baixo dos panos.
* Para entender como _decorators_ funcionam, precisamos primeiro entender alguns conceitos sobre funções.

### 01_funcoes_objetos_de_primeira_classe.py
* Em Python, ser um objeto de primeira classe significa que funções podem ser salvas em variávies, usadas ou passadas como argumentos e retornadas de outras funções.
  * É possível salvar funções dentro de estruturas de dados, como listas, dicionários, _sets_, etc.
* **Funções aninhadas** (_nested functions_): funções definidas dentro de outra função.
  * Podemos definir funções dentro de outra função.
  * O escopo principal não conhece as funções internas.
  * Só é possível chamar a função interna dentro do escopo da função externa.
```python
def funcao_de_fora():
  print('Iniciando função de fora')
  # A função definida abaixo é aninhada
  def funcao_de_dentro():
    print('Executando função de dentro')
  
  funcao_de_dentro()
  print('Finalizando função de fora')
```
* É possível salvar uma função em uma variável e passá-la como parâmetro para outra função.
```python
def executar(func):
  func()

def funcao():
  print('oi mundo')

func = funcao
print(executar(func)) # oi mundo
```
* É possível retornar uma função de outra.
```python
def executar(func, x, y):
  return func(x, y)

def potencia(x, exp):
  return x ** exp

resultado = executar(potencia, 5, 2) # 25
```

### 02_decorators.py
* Os _decorators_ são funções que envolvem outras funções, modificando seu comportamento.
  * Um _decorator_ permite adicionar qualquer comportamento antes ou depois de outra função.
```python
def logger(func):
  def wrapper(x):
    print('Começando a função')
    func(x)
    print('Terminando a função')
  return wrapper

@logger
def funcao():
  # realiza operacao
```
* Exemplos de uso de decorators:
  * Log: Imprimir no log que a função está sendo usada.
  * Segurança: Garantir que o usuário esteja logado e tenha permissão antes de executar uma função no servidor
  * Medição de performance: Calcular o tempo de execução de uma função.
  * Roteador: especificar que a função deve ser chamada quando uma requisição HTTP chegar ao servidor.

## Desafio 13
Resolva o desafio proposto no [arquivo do desafio](./03_desafio_13.py)

## APIs
Introdução: slide.

### 04_http_get.py
* O módulo `requests` da biblioteca padrão possui funções que permitem chamar APIs RESTful.
* Quando digitamos uma URL na barra de endereço do navegador, ele faz uma requisição de GET para essa URL, que responde com um conteúdo em HTML.
* A resposta vem com o código que indica se a requisição foi bem sucedida ou não, assim como outras coisas interessantes.
* A biblioteca `requests` provê a função `get()` para realizar este tipo de requisição.
* Os metadados da resposta vêm no cabeçalho `resposta.headers` e podem ser "fiscalizados" mais facilmente utilizando o debugger do VSCode.
  * O cabeçalho `content-type` indica o tipo do arquivo que foi retornado.
* O conteúdo da resposta vem na variável `resposta.text`.
* Enviando uma requisição GET para a página do [ConstruDelas](http://womakerscode.org/construdelas/), recebemos como resposta um documento no formato `text/html` contendo todo código HTML da página.
* O GET também permite chamar funções em servidores. 
* É possível buscar dados sobre o clima em uma determinada coordenada geográfica com a API do site [OpenWeather](https://openweathermap.org/current).
* Os parâmetros são salvos em um dicionário, e incluídos como o segundo argumento da função `get()`.
* O conteúdo é retornado no formato JSON, e pode ser lido pela biblioteca `json` como já vimos anteriormente.
* Para saber qual o formato de retorno e como acessar os campos necessários para a nossa aplicação, utilizamos a documentação da API.
  * Essa documentação é um contrato, e garante que o resultado sempre vai ser retornado no formato descrito.

### 05_http_outros_verbos.py
* Para os outros verbos HTTP, vamos acessar os exemplos providos pela página [HTTP Bin](https://httpbin.org/).

### 06_erros.py
* Existem diversos códigos possíveis que indicam erros que podemos ter em uma API
* É comum as APIs exigirem que nós enviemos alguma chave para indicar que podemos acessar um recurso.
  * A chave é vinculada a uma determinada conta e pode ter uma data de validade.
  * A chave pode ser enviada como parâmetro da requisição.
  * A requisição é criptografada ponta a ponta pelo protocolo HTTPS.
* Se deixamos de enviar a chave que prova que somos um usuário do site, recebemos o código de erro 401.
  * A solução do código 401 é buscar uma chave válida com o servidor ao qual estamos acessando.
* Se esquecemos de mandar um parâmetro obrigatório, recebemos o código 400 (requisição inválida).
* O código 404 é o mais fomoso. Ele indica que a página não existe.
* Se tentamos fazer uma requisição PUT para uma URL que não aceita este método, vamos receber o erro 405.
* Como lidar com erros?
  * Sempre teste o código de retorno da API antes executar as funcionalidades do servidor.
  * A forma de lidar com um erro depende do erro, logo depende de qual código foi retornado.
    * Ex: Se for um erro de autenticação ou autorização, retorne 401 ou 403 e peça para o usuário usar as credenciais corretas.
  * Sempre retorne o código correto para o front-end.
  * Se o seu back-end depende de uma API que retornou um erro, você pode retornar como resposta para o front-end o erro 500.
  * Redundância: podemos ter múltiplas cópias de um servidor de backend para caso um venha a dar problema, nossa aplicação chamar o mesmo método em outra.

## Desafio Offline - Microsoft Learn
* Complete o módulo ["Explorar o mundo das artes usando APIs RESTful"](https://docs.microsoft.com/pt-br/learn/modules/use-apis-discover-museum-art/ ).
* Não esqueça de adicionar o PDF que comprova que você completou este módulo [na pasta de selos](../selos_microsoft_learn/).