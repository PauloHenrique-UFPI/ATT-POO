from conta import Conta
from conta import Cliente
from cadastro import Cadastro

cliente1 = Cliente('Carlos','Borges', 100001)


pessoa = Conta(cliente1,1234,5000.00,20000.00)


print(pessoa)

print('\nNumero de contas: ', Conta.total_contas())
