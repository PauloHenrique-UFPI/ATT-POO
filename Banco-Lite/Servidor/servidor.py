from conta import Cliente
from conta import Conta
from cadastro import Cadastro
from cadastroConta import Cadastro_Conta
import socket
#alteracao do banco de dados
import sqlite3


host = 'localhost'
port = 8100
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(1000)
cad = Cadastro()
cadConta = Cadastro_Conta()

#alteracao do banco de dados
conexao = sqlite3.connect('bd_lite.sqlite')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS contas_banco(id integer PRIMARY KEY, nome text NOT NULL, sobrenome text NOT NULL, cpf text NOT NULL, numero text NOT NULL,  saldo float NOT NULL,  limite text NOT NULL);"""

cursor.execute(sql)
print('Aguardando conexao...')

con, cliente = serv_socket.accept()
print('Conectado')
print('Aguardando mensagem...')

cont = 0
cursor.execute('SELECT * from contas_banco')

aux = 0;
for info in cursor:
    p = Cliente(info[1],info[2],info[3])
    c = Conta(p,info[4],info[5],info[6])
    cadConta.cadastra(c)
    print('\nnumero da Conta: ',c.numero())
    aux = info[4]
   
# cursor.execute('UPDATE contas_banco SET saldo = c.saldo WHERE id = 0')

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
        recebeOp = con.recv(1024).decode()
        con.send(str(aux).encode())
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
            cursor.execute('INSERT INTO contas_banco(nome, sobrenome, cpf, numero, saldo, limite) VALUES(?,?,?,?,?,?)',(p.nome,p.sobrenome,p.cpf,recebeCout,0,'10000'))
            con.send('True'.encode())
            aux = int(recebeCout)
            conexao.commit()

        else:
            con.send('False'.encode())

        continue     
    
    if recebeOp == 'sacar':
        recebeCAtual = con.recv(1024).decode()
        c = cadConta.busca(recebeCAtual)
        if c != None:
            con.send('True'.encode())
            recebeValor = con.recv(1024).decode()
            if c.sacar(int(recebeValor)):
                con.send('True'.encode())
                #update dos saldo
                cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeCAtual))
                for info in cursor:
                    aux = info[0]
                cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(c.saldo_conta(),info[0]))
                conexao.commit()
            else:
                con.send('False'.encode())
            continue

        else:
            con.send('False'.encode())
            continue

    if recebeOp == 'depositar':
        recebeCAtual = con.recv(1024).decode()
        c = cadConta.busca(recebeCAtual)
        print(c.numero())
        if c != None:
            con.send('True'.encode())
            recebeValor = con.recv(1024).decode()
            if c.depositar(float(recebeValor)):
                con.send('True'.encode())
                #update dos saldo
                cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeCAtual))
                for info in cursor:
                    aux = info[0]
                cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(c.saldo_conta(),info[0]))
                conexao.commit()
            else:
                con.send('False'.encode())
            continue

        else:
            con.send('False'.encode())
            continue

    if recebeOp == 'extrato':
        recebeCAtual = con.recv(1024).decode()
        c = cadConta.busca(recebeCAtual)
        if c != None:
            con.send('True'.encode())
            con.recv(1024).decode()
            data = Conta.data(c)
            saldo = Conta.saldo_conta(c)
            con.send(str(data).encode())
            con.recv(1024).decode()
            con.send(str(saldo).encode())
        else:
            con.send('False'.encode())
        continue

    if recebeOp == 'historico':
        recebeCAtual = con.recv(1024).decode()
        c = cadConta.busca(recebeCAtual)
        if c != None:
            con.send('True'.encode())
            historico = Conta.historico(c)
            for lp in historico:
                con.recv(1024).decode()
                con.send(lp.encode())
            con.recv(1024).decode()
            con.send('False'.encode())
            continue
        else:
            con.send('False'.encode())
        continue
    
    if recebeOp == 'tranferir':
        recebeConta = con.recv(1024).decode()
        c = cadConta.busca(recebeConta)
    if c != None:
        con.send('True'.encode())
        recebeConta1 = con.recv(1024).decode()
        c1 = cadConta.busca(recebeConta1)
        if c1 != None:
            con.send('True'.encode())
            recebeValor = con.recv(1024).decode()
            if c.transfere(c1,float(recebeValor)):
                con.send('True'.encode())
                cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeCAtual))
                for info in cursor:
                    aux = info[0]
                cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(c.saldo_conta(),info[0]))
                conexao.commit()
            else:
                con.send('False'.encode())
            continue
        else:
            con.send('False'.encode())
            continue
    else:
        con.send('False'.encode())
    continue
serv_socket.close()


        






                    

   

