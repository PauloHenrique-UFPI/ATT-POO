import socket
from conta import Cliente
from conta import Conta
from cadastro import Cadastro
from cadastroConta import Cadastro_Conta

host = 'localhost'
port = 8100
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(1000)
cad = Cadastro()
cadConta = Cadastro_Conta()

print('Aguardando conexao...')

con, cliente = serv_socket.accept()
print('Conectado')
print('Aguardando mensagem...')

cont = 0
while True:

    recebeOp = con.recv(1024).decode()
    con.send('opcao recebida'.encode())

    if recebeOp == 'cad_pessoa':
        recebeNome = con.recv(1024).decode()
        con.send('nome recebido'.encode())
        recebeSobrenome = con.recv(1024).decode()
        con.send('sobrenome recebido'.encode())
        recebeCpf = con.recv(1024).decode()
        p = Cliente(recebeNome,recebeSobrenome,recebeCpf)
        if(cad.cadastra(p)):
            con.send('True'.encode())
        else:
            con.send('False'.encode())
            
        continue

    if recebeOp == 'cad_conta':
        recebeCpf = con.recv(1024).decode()
        if cad.busca(recebeCpf):
            print(cad.busca(recebeCpf))
            con.send('True'.encode())
        else:
            print(cad.busca(recebeCpf))
            con.send('False'.encode())
            continue


        recebeCout = con.recv(1024).decode()
        print('conta: ', recebeCout)
        c = Conta(p,recebeCout,0,10000)
        if cadConta.cadastra(c):
            con.send('True'.encode())
        else:
            con.send('False'.encode())
        
        continue     
    
    '''
    #operacao
    while cont < 3:
        if cont == 0:
            recebeNumeroConta = con.recv(1024).decode()
        elif cont == 1:
            recebeOperacao = con.recv(1024).decode()
        elif cont == 2:
            recebeValor = con.recv(1024).decode()
            if recebeValor != -1:
                int(recebeValor)
        cont+=1
        
    print('Numero da conta: ',recebeNumeroConta,'\nOperacao: ', recebeOperacao, '\nValor: ', recebeValor)
    cont = 0

    if recebeNumeroConta == '-1':
        break
    '''        
   

serv_socket.close()