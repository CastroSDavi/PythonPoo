
from PythonPoo.Banco.banco import Banco
from PythonPoo.Banco.pessoa import Cliente



cliente1 = Cliente('Davi', 20)
cliente1.adicionar_conta_corrente(101, 20, 1000, 100)
santander = Banco()
santander.adicionar_cliente(cliente1)
print(cliente1.conta.agencia)

cliente1.conta.deposito(500)