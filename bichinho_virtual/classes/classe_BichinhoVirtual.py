from random import randint
from typing import Type
from classe_comida import Comida


class BichinhoVirtual:

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__saciedade = 100
        self.__sociabilidade = 100
        self.__higiene = 100
        self.__energia = randint(0, 100)

# metodos getters e setters
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def saciedade(self) -> int:
        return self.__saciedade

    @saciedade.setter
    def saciedade(self, saciedade: int) -> None:
        if isinstance(saciedade, int):
            self.__saciedade = saciedade

    @property
    def sociabilidade(self) -> int:
        return self.__sociabilidade

    @sociabilidade.setter
    def sociabilidade(self, sociabilidade: int) -> None:
        if isinstance(sociabilidade, int):
            self.__sociabilidade = sociabilidade

    @property
    def higiene(self) -> int:
        return self.__higiene

    @higiene.setter
    def higiene(self, higiene: int) -> None:
        if isinstance(higiene, int):
            self.__saciedade = higiene

    @property
    def energia(self) -> int:
        return self.__energia

    @energia.setter
    def energia(self, energia: int) -> None:
        if isinstance(energia, int):
            self.__energia = energia

# metodos
    def alimentar(self, comida: Type[Comida]) -> None:
        if self.__saciedade == 100:
            print('Estou cheio')
        elif self.__saciedade + comida.saciedade > 100:
            self.saciedade = 100
        else:
            self.saciedade += comida.saciedade

    def conversar(self) -> None:
        if self.__sociabilidade == 100:
            print('Quero ficar um pouco sozinho')
        elif self.__sociabilidade + 10 > 100:
            self.__sociabilidade = 100
        else:
            self.sociabilidade += 10

    def limpar(self) -> None:
        if self.__higiene == 100:
            print('Já estou muito limpo')
        elif self.__higiene + 10 > 100:
            self.__higiene = 100
        else:
            self.__higiene += 10

    def dormir(self) -> None:
        if self.__energia == 100:
            print('Estou sem sono')
        elif self.__energia + 10 > 100:
            self.__energia = 100
        else:
            self.energia += 10

    def status(self) -> None:
        print(f'''
        status
saciedade: {self.__saciedade}%
sociabilidade:{self.__sociabilidade}%
higiene:{self.__higiene}%
Energia:{self.__energia}%
        ''')
        
