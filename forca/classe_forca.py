class Forca:

    def __init__(self, palavra: str, erros: int ):
        self.palavra = palavra
        self.erros = erros
        self.palavra_apoio = list('-' for _ in range(len(self.palavra)))

    def __escolher_letra(self):
        while True:
            letra_escolhida = str(input('Digite uma letra: ')).lower()
            if (self.__verificar_tamanho_da_letra(letra_escolhida) and self.__verificar_tipo(letra_escolhida)):
                return letra_escolhida
            
            print('Digite novamente')
    
    def __verificar_tamanho_da_letra(self, letra_escolhida):
        tamanho = int(len(letra_escolhida))
        if tamanho > 1:
            return False
        
        return True

    def __verificar_tipo(self, letra_escolhida):
        if not letra_escolhida.isalpha():
            return False

        return True

    def __procurar_letra(self, letra_escolhida):
        if letra_escolhida in self.palavra:
            for contador, letra in enumerate(self.palavra):
                if letra_escolhida == letra:
                    self.palavra_apoio[contador] = letra
                    print(''.join(self.palavra_apoio))
        else:
            self.erros -= 1

    def jogar(self):
        print(''.join(self.palavra_apoio))
        while True:
            self.__procurar_letra(self.__escolher_letra())
            if not '-' in self.palavra_apoio:
                print('Parabéns, você ganhou')
                break
            elif self.erros == 0:
                print('Que pena, você perdeu')
                break
