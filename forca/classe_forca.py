class Forca:

    def __init__(self, palavra: str, erros: int ):
        self.palavra = palavra
        self.erros = erros
        self.palavra_apoio = list('-' for _ in range(len(self.palavra)))

    @staticmethod
    def __inserir_letra() -> str:
        letra_escolhida = str(input('\nDigite uma letra:')).lower()
        return letra_escolhida

    def __procurar_letra(self, letra_escolhida):
        if letra_escolhida in self.palavra:
            for contador, letra in enumerate(self.palavra):
                if letra_escolhida == letra:
                    self.palavra_apoio[contador] = letra
                    print(''.join(self.palavra_apoio))
        else:
            self.erros -= 1
    
    def __verificar_resultado(self):
        pass

    def jogar(self):
        print(''.join(self.palavra_apoio))
        while True:
            self.__procurar_letra(self.__inserir_letra())
