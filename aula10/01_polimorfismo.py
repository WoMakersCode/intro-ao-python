# len() utiliza polimorfismo. Ela pode receber como parâmetro
# objetos de diferentes tipos e ela sabe contar quantos itens
# existem mesmo assim.
print('Função len():')
print(len("ConstruDelas"))
print(len([10, 20, 30]))

# Podemos criar uma função que aceita tipos diferentes de parâmetros,
# permitindo assim o polimorfismo.
class Brasil:
    def __init__(self):
        self.__capital = 'Brasilia'
        self.__lingua = 'Português Brasileiro'

    @property
    def capital(self):
        return self.__capital

    @property
    def lingua(self):
        return self.__lingua

class EstadosUnidos:
    def __init__(self):
        self.__capital = 'Washington'
        self.__lingua = 'Inglês'

    @property
    def capital(self):
        return self.__capital

    @property
    def lingua(self):
        return self.__lingua

def processar_pais(objeto):
    print(type(objeto))
    print(objeto.capital)
    print(objeto.lingua)

brasil = Brasil()
eua = EstadosUnidos()

processar_pais(brasil)
processar_pais(eua)
print()

# Polimorfismo com herança
class Animal:
    def __init__(self):
        self.__numero_patas = -1
        self.__tem_asas = False

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas

    def emitir_som(self):
        print('...')

class Cachorro(Animal):
    def __init__(self):
        self.__numero_patas = 4
        self.__tem_asas = False

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas

    # Se não sobrescrever o método, o método usado vai ser o herdado da classe pai
    # def emitir_som(self):
    #     print('auau')

    def fazer_truque(self):
        print('Sento e deito')

class Gato(Animal):
    def __init__(self):
        self.__numero_patas = 4
        self.__tem_asas = False

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas

    def emitir_som(self):
        print('miau')

class Calopsita(Animal):
    def __init__(self):
        self.__numero_patas = 2
        self.__tem_asas = True

    @property
    def numero_patas(self):
        return self.__numero_patas

    @property
    def tem_asas(self):
        return self.__tem_asas

    def emitir_som(self):
        print('piuuuu')

    def voar(self):
        print('to voando')

def processar_animal(animal: Animal):
    print(f'Este animal tem {animal.numero_patas} patas')
    print(f'Este animal tem asas? {animal.tem_asas}')
    animal.emitir_som()
    if isinstance(animal, Calopsita):
        animal.voar()
    if isinstance(animal, Cachorro):
        animal.fazer_truque()
    print()
    

cachorro = Cachorro()
gato = Gato()
calopsita = Calopsita()

processar_animal(cachorro)
processar_animal(gato)
processar_animal(calopsita)