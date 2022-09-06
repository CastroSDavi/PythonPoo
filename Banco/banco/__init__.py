class Banco:

    def __init__(self):
        self.agencias = list(x for x in range(100, 1000))
        self.clientes = list()

    def adicionar_cliente(self, cliente):
        if self.__verificar_agencia(cliente):
            self.clientes.append(cliente)
            print('Cliente adicionado')
        else:
            print('A agência não pertence a esse banco')

    def autenticar_cliente(self, cliente):
        if cliente in self.clientes:
            print('Cliente autenticado')
        else:
            print('Cliente não cadastrado')

    def __verificar_agencia(self, cliente):
        if cliente.conta.agencia in self.agencias:
            return True

        return False
