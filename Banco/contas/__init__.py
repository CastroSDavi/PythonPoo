from abc import ABC, abstractmethod


class ContaInterface(ABC):

    @abstractmethod
    def saque(self, valorsacado: float):
        pass

    @abstractmethod
    def deposito(self, valordepositado: float):
        pass


class ContaCorrente(ContaInterface):

    def __init__(self, agencia: int, conta: int, saldo=0, limite=100) -> None:
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo
        self.__limite = limite

    @property
    def agencia(self) -> int:
        return self.__agencia

    @property
    def conta(self) -> int:
        return self.__conta

    @property
    def saldo(self) -> int:
        return self.__saldo

    @property
    def limite(self) -> int:
        return self.__limite

    def saque(self, valorsacado: float) -> None:
        if self.__valid_num(valorsacado):
            if self.__valid_saque(valorsacado):
                self.__saldo -= valorsacado
                print(f'Saque realizado \nValor sacado = {valorsacado}R$')
                self.detalhes()
            else:
                print(f'Saldo insuficiente \nSaldo = {self.__saldo}R$')
        else:
            print('valor inválido, insira um número')

    def deposito(self, valordepositado: float) -> None:
        if self.__valid_num(valordepositado):
            self.__saldo += valordepositado
            print(f'Depósito realizado \nValor depositado = {valordepositado}R$')
            self.detalhes()
        else:
            print('valor inválido, insira um número')

    def detalhes(self) -> None:
        print(f'Dados:\n'
              f'número da agência = {self.__agencia}\n'
              f'número da conta = {self.__conta}\n'
              f'saldo disponível = {self.__saldo}RS')

    def __valid_saque(self, valorsacado: float) -> bool:
        if self.__saldo + self.__limite < valorsacado:
            return False
        else:
            return True

    @staticmethod
    def __valid_num(valor) -> bool:
        if isinstance(valor, (int, float)):
            return True
        else:
            return False


class ContaPoupanca(ContaInterface):
    def __init__(self, agencia: int, conta: int, saldo=0) -> None:
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self) -> int:
        return self.__agencia

    @property
    def conta(self) -> int:
        return self.__conta

    @property
    def saldo(self) -> float:
        return self.__saldo

    def saque(self, valorsacado: float) -> None:
        if self.__valid_saque(valorsacado):
            self.__saldo -= valorsacado
            print(f'Saque realizado \nValor sacado = {valorsacado}R$')
            self.detalhes()
        else:
            print(f'Saldo insuficiente \nSaldo = {self.__saldo}R$')

    def deposito(self, valordepositado) -> None:
        if self.__valid_num(valordepositado):
            self.__saldo += valordepositado
            print(f'Deposito realizado \nValor depositado = {valordepositado}R$')
            self.detalhes()
        else:
            print('valor inválido, insira um número')

    def detalhes(self) -> None:
        print(f'Dados:\n'
              f'número da agência = {self.__agencia}\n'
              f'número da conta = {self.__conta}\n'
              f'saldo disponível = {self.__saldo}R$')

    def __valid_saque(self, valorsacado: float) -> bool:
        if self.__saldo - valorsacado < 0:
            return False
        else:
            return True

    @staticmethod
    def __valid_num(valor) -> bool:
        if isinstance(valor, (int, float)):
            return True
        else:
            return False
