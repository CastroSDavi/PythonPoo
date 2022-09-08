class Jogador:
    def __init__(self, simbolo, pontuacao = 0) -> None:
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
    def pontuacao(self,valor):
        self.__pontuacao = valor

class JogoDaVelha:
    
    def __init__(self) -> None:
        self.pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.jogador1 =  Jogador('X')
        self.jogador2 = Jogador('O')

    def __repr__(self):
        return 'Jogo da velha, Autor: Davi Castro'

    @staticmethod
    def __introducao() -> None:
        print('-' * 25)
        print(f'{"Jogo da Velha":-^25}')
        print('-' * 25)

    @staticmethod
    def __validar_jogada(msg: str) -> int:
        while True:
            try:
                num = int(input(msg)) - 1
                if num > 8 or num < 0:
                    print('Digite um número inteiro entre 1 e 9')
                    continue
            except ValueError:
                print('Digite um número inteiro')
            else:
                return num

    def __mostrar_tabuleiro(self) -> None:
        print(f'\t{self.pos[0]} | {self.pos[1]} | {self.pos[2]}\n'
              f'\t----------\n'
              f'\t{self.pos[3]} | {self.pos[4]} | {self.pos[5]}\n'
              f'\t----------\n'
              f'\t{self.pos[6]} | {self.pos[7]} | {self.pos[8]}')

    def __fazer_jogada(self, simbolo: str) -> None:
        while True:
            num = self.__validar_jogada('\nDigite uma posição entre 1 e 9: ')
            if self.pos[num] == ' ':
                self.pos[num] = simbolo
                break
            else:
                print('Posição inválida')

    def __verificar_vencedor(self, simbolo: str) -> bool:
        if self.pos[0] == simbolo and self.pos[1] == simbolo and self.pos[2] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[3] == simbolo and self.pos[4] == simbolo and self.pos[5] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[6] == simbolo and self.pos[7] == simbolo and self.pos[8] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[0] == simbolo and self.pos[3] == simbolo and self.pos[6] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[1] == simbolo and self.pos[4] == simbolo and self.pos[7] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[2] == simbolo and self.pos[5] == simbolo and self.pos[8] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[0] == simbolo and self.pos[4] == simbolo and self.pos[8] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True
        elif self.pos[2] == simbolo and self.pos[4] == simbolo and self.pos[6] == simbolo:
            print(f'{simbolo} é o vencedor')
            return True

        return False

    def __definir_pontuacao(self, vencedor):
        pass

    def jogar(self):
        self.__introducao()
        while True:
            self.__mostrar_tabuleiro()
            self.__fazer_jogada(self.jogador1.simbolo)
            if self.__verificar_vencedor(self.jogador1.simbolo):
                self.__mostrar_tabuleiro()
                break
            if ' ' not in self.pos:
                self.__mostrar_tabuleiro()
                print('Empate')
                break
            self.__mostrar_tabuleiro()
            self.__fazer_jogada(self.jogador2.simbolo)
            if self.__verificar_vencedor(self.jogador2.simbolo):
                self.__mostrar_tabuleiro()
                break


jogo = JogoDaVelha()
jogo.jogar()