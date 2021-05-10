from conta import Conta
from conta import Cliente

cliente1 = Cliente('Carlos','Borges', 100001)
cliente2 = Cliente('Maria','Eduarda', 100002)

pessoa = Conta(cliente1,1234,5000.00,20000.00)
pessoa2 = Conta(cliente2,5575,1000.00,5000.00)

pessoa.depositar(500)
pessoa.sacar(100)
pessoa.extrato()
pessoa.transfere(pessoa2,500)
pessoa.extrato()

pessoa2.extrato()

pessoa.mostra_historico()
pessoa2.mostra_historico()

print('\nNumero de contas: ', Conta.total_contas())
