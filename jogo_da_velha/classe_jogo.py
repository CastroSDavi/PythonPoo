from classe_Jogador import Jogador


class JogoDaVelha:
    
    def __init__(self) -> None:
        self.pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.jogador1 =  Jogador('X')
        self.jogador2 = Jogador('O')

    def __repr__(self):
        return 'Jogo da velha, Autor: Davi Castro'

    @staticmethod
    def __introducao() -> None:
        print('-' * 30)
        print(f'{"Jogo da Velha": ^30}')
        print('-' * 30)

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
        print('''
          {} | {} | {}
        -------------
          {} | {} | {}
        -------------
          {} | {} | {}'''.format(
            self.pos[0], self.pos[1], self.pos[2],
            self.pos[3], self.pos[4], self.pos[5],
            self.pos[6], self.pos[7], self.pos[8]))

    def __fazer_jogada(self, jogador) -> None:
        while True:
            num = self.__validar_jogada('\nDigite uma posição entre 1 e 9: ')
            if self.pos[num] == ' ':
                self.pos[num] = jogador.simbolo
                break
            else:
                print('Posição inválida')

    def __verificar_vencedor(self, jogador) -> bool:
        if self.pos[0] == jogador.simbolo and self.pos[1] == jogador.simbolo and self.pos[2] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[3] == jogador.simbolo and self.pos[4] == jogador.simbolo and self.pos[5] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[6] == jogador.simbolo and self.pos[7] == jogador.simbolo and self.pos[8] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[0] == jogador.simbolo and self.pos[3] == jogador.simbolo and self.pos[6] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[1] == jogador.simbolo and self.pos[4] == jogador.simbolo and self.pos[7] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[2] == jogador.simbolo and self.pos[5] == jogador.simbolo and self.pos[8] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[0] == jogador.simbolo and self.pos[4] == jogador.simbolo and self.pos[8] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif self.pos[2] == jogador.simbolo and self.pos[4] == jogador.simbolo and self.pos[6] == jogador.simbolo:
            print(f'{jogador.simbolo} é o vencedor')
            self.__aumentar_pontuacao(jogador)
            return True
        elif ' ' not in self.pos:
            print('Empate')
            return True

        return False

    def __aumentar_pontuacao(self, jogador):
        jogador.pontuacao += 1

    def __mostrar_placar(self):
        print('''
------------------------------
     {} - {}    |    {} - {}
------------------------------
        '''.format(
            self.jogador1.simbolo,
            self.jogador1.pontuacao,
            self.jogador2.pontuacao,
            self.jogador2.simbolo))

    def __restart(self):
        self.pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def jogar(self):
        self.__introducao()
        while True:
            self.__mostrar_placar()
            self.__mostrar_tabuleiro()
            self.__fazer_jogada(self.jogador1)
            if self.__verificar_vencedor(self.jogador1):
                self.__mostrar_placar()
                self.__mostrar_tabuleiro()
                break
            self.__mostrar_placar()
            self.__mostrar_tabuleiro()
            self.__fazer_jogada(self.jogador2)
            if self.__verificar_vencedor(self.jogador2):
                self.__mostrar_placar()
                self.__mostrar_tabuleiro()
                break
            