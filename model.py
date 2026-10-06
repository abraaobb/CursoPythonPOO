from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Atleta(Pessoa):
    def __init__(self, nome, idade, altura, peso):
        super().__init__(nome, idade)
        self.altura = altura
        self.peso = peso

    def mostrar(self):
        pass


class Corredor(Atleta):
    def __init__(self, distancia, tenis, pace, **kwargs):
        super().__init__(**kwargs)
        self.distancia = distancia
        self.tenis = tenis
        self.pace = pace

    def correr(self):
        print("Estou correndo\n")

    def mostrar(self):
        print(f'Nome: {self.nome}\n'
              f'Idade: {self.idade}'
              f'\nAltura: {self.altura}'
              f'\nPeso: {self.peso}'
              f'\nDistancia: {self.distancia},'
              f'\nTenis: {self.tenis}'
              f'\nPace: {self.pace}')


class Nadador(Atleta):
    def __init__(self, sunga, touca, oculos, **kwargs):
        super().__init__(**kwargs)
        self.sunga = sunga
        self.touca = touca
        self.oculos = oculos

    def nadar(self):
        print("Estou nadando\n")


class Ciclista(Atleta):
    def __init__(self, bike, capacete, **kwargs):
        super().__init__(**kwargs)
        self.bike = bike
        self.capacete = capacete

    def pedalar(self):
        print("Estou pedalando\n")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, categoria='amador', **kwargs):
        super().__init__(**kwargs)
        self.categoria = categoria

    def fazer_prova(self):
        self.nadar()
        self.pedalar()
        self.correr()


class DispositivoEletronico(ABC):
    def __init__(self, marca):
        self.marca = marca
        self.ligado = False

    def ligado(self):
        self.ligado = True

    def desligado(self):
        self.ligado = False

    @abstractmethod
    def descricao(self):
        pass

    def outro_metodo(self):
        pass


class Televisao(DispositivoEletronico):
    def __init__(self, marca, polegadas):
        super().__init__(marca)
        self.polegadas = polegadas

    def descricao(self):
        print(f"Televisao {self.marca} tem {self.polegadas} polegadas")
