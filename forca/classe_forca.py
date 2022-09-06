class Forca:

    def __init__(self):
        self.palavra = None
        self.erros = None

    @staticmethod
    def __introducao():
        print('-' * len('jogo da forca'))
        print('jogo da forca'.upper())
        print('-' * len('jogo da forca'))

    def __inserir_palavra(self):
        palavra = str(input('\nDigite uma palavra:'))
        self.palavra = palavra

    def __definir_numero_erros(self):
        erros = int(input('Digite o número máximo de erros:'))
        self.erros = erros

    def jogar(self):
        self.__introducao()
        self.__inserir_palavra()
        self.__definir_numero_erros()
        contador_erros = 0
        palavra_apoio = list('-' for _ in range(len(self.palavra)))
        print('')
        print(''.join(palavra_apoio))

        while True:
            letra_escolhida = str(input('\nDigite uma letra:'))
            if letra_escolhida in self.palavra:
                for contador, letra in enumerate(self.palavra):
                    if letra == letra_escolhida:
                        palavra_apoio[contador] = letra
                print('')
                print((''.join(palavra_apoio)))
            else:
                contador_erros += 1
                if contador_erros == self.erros:
                    print("Você, perdeu")
                    break


forca = Forca()

forca.jogar()
