class Jogador:
    def __init__(self, simbolo, pontuacao=0) -> None:
        self.__simbolo = simbolo
        self.__pontuacao = pontuacao 
    
    @property
    def simbolo(self):
        return self.__simbolo
    
    @simbolo.setter
    def simbolo(self, valor):
        self.__simbolo = valor

    @property
    def pontuacao(self):
        return self.__pontuacao
    
    @pontuacao.setter
    def pontuacao(self, valor):
        self.__pontuacao = valor