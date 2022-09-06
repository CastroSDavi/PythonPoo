from Banco.contas import ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade


class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.__conta = None

    @property
    def conta(self):
        return self.__conta

    def adicionar_conta_corrente(self, agencia: int, conta: int, saldo: float, limite=100) -> None:
        self.__conta = ContaCorrente(agencia, conta, saldo, limite)
        print('Conta corrente criada')

    def adicionar_conta_poupanca(self, agencia: int, conta: int, saldo: float) -> None:
        self.__conta = ContaPoupanca(agencia, conta, saldo)
        print('Conta poupança criada')
