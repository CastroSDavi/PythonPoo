class Comida:

    def __init__(self, nome: str, saciedade: int) -> None:
        self.__nome = nome
        self.__saciedade = saciedade

    @property
    def nome(self) -> str:
        return self.__nome
 
    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome

    @property
    def saciedade(self) -> int:
        return self.__saciedade
     
    @saciedade.setter
    def saciedade(self, saciedade) -> None:
        self.__saciedade = saciedade
