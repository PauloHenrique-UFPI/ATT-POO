from mysql.connector.constants import ServerFlag
from conta import Cliente
from conta import Conta
from cadastro import Cadastro
from cadastroConta import Cadastro_Conta
import socket
#alteracao do banco de dados
import mysql.connector as mysql
import threading

class ClienteThread(threading.Thread):
    def __init__(self, clientAddress, clientesocket, numero, aux: int, aux_id: int, sinc):
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.numero = numero
        self.aux = aux
        self.aux_id = aux_id
        self.sinc = sinc
        print("Nova conexao: ",clientAddress)

    def run(self):
        print("Conectado de: ", ClientAddress)
        self.sinc.acquire()
        self.operacao()
        self.sinc.release()

    

    def operacao(self):
        recebeOp = self.csocket.recv(1024).decode()
        self.csocket.send('opcao recebida'.encode())


        if recebeOp == 'cad_pessoa':
            recebeNome = self.csocket.recv(1024).decode()
            self.csocket.send('nome recebido'.encode())
            recebeSobrenome = self.csocket.recv(1024).decode()
            self.csocket.send('sobrenome recebido'.encode())
            recebeCpf = self.csocket.recv(1024).decode()
            p = Cliente(recebeNome,recebeSobrenome,recebeCpf)
            print('opcao: ',recebeCpf)
            print(recebeCpf)
            if(cad.cadastra(p)):
                self.csocket.send('True'.encode())
            else:
                self.csocket.send('False'.encode())
            
        
        if recebeOp == 'cad_conta':
            recebeOp = self.csocket.recv(1024).decode()
            self.csocket.send(str(self.aux).encode())
            recebeCpf = self.csocket.recv(1024).decode()
            if cad.busca(recebeCpf):
                print(cad.busca(recebeCpf))
                self.csocket.send('True'.encode())
            else:
                print(cad.busca(recebeCpf))
                self.csocket.send('False'.encode())
            recebeCout = self.csocket.recv(1024).decode()
            print('conta: ', recebeCout)
            c = Conta(p,recebeCout,0,10000)
            if cadConta.cadastra(c):
                self.aux_id += 1
                cursor.execute("INSERT INTO contas_banco(id, nome, sobrenome, cpf, numero, saldo, limite) VALUES({},%s,%s,{},{},{},{})".format(self.aux,p.cpf,recebeCout,'0','10000'),(p.nome,p.sobrenome))
                self.csocket.send('True'.encode())
                self.aux = int(recebeCout)
                conexao.commit()
            else:
                self.csocket.send('False'.encode())

        if recebeOp == 'sacar':
            print('entrou em sacar')
            recebeCAtual = self.csocket.recv(1024).decode()
            c = cadConta.busca(recebeCAtual)
            if c != None:
                self.csocket.send('True'.encode())
                recebeValor = self.csocket.recv(1024).decode()
                if c.sacar(int(recebeValor)):
                    self.csocket.send('True'.encode())
                    #update dos saldo
                    cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeCAtual))
                    for info in cursor:
                        self.aux = info[0]

                    cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(str(c.saldo_conta()),info[0]))
                    conexao.commit()
                else:
                    self.csocket.send('False'.encode())
            else:
                self.csocket.send('False'.encode())

        if recebeOp == 'depositar':
            recebeCAtual = self.csocket.recv(1024).decode()
            c = cadConta.busca(recebeCAtual)
            if c != None:
                self.csocket.send('True'.encode())
                recebeValor = self.csocket.recv(1024).decode()
                if c.depositar(float(recebeValor)):
                    self.csocket.send('True'.encode())
                    #update dos saldo
                    cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeCAtual))
                    for info in cursor:
                        self.aux = info[0]
                    cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(str(c.saldo_conta()),info[0]))
                    conexao.commit()
                else:
                    self.csocket.send('False'.encode())
            else:
                self.csocket.send('False'.encode())

        if recebeOp == 'extrato':
            recebeCAtual = self.csocket.recv(1024).decode()
            c = cadConta.busca(recebeCAtual)
            if c != None:
                self.csocket.send('True'.encode())
                self.csocket.recv(1024).decode()
                data = Conta.data(c)
                saldo = Conta.saldo_conta(c)
                self.csocket.send(str(data).encode())
                self.csocket.recv(1024).decode()
                self.csocket.send(str(saldo).encode())
            else:
                self.csocket.send('False'.encode())

        if recebeOp == 'historico':
            recebeCAtual = self.csocket.recv(1024).decode()
            c = cadConta.busca(recebeCAtual)
            if c != None:
                self.csocket.send('True'.encode())
                historico = Conta.historico(c)
                for lp in historico:
                    self.csocket.recv(1024).decode()
                    self.csocket.send(lp.encode())
                self.csocket.recv(1024).decode()
                self.csocket.send('False'.encode())
            else:
                self.csocket.send('False'.encode())

        if recebeOp == 'tranferir':
            recebeConta = self.csocket.recv(1024).decode()
            c = cadConta.busca(recebeConta)
            if c != None:
                self.csocket.send('True'.encode())
                recebeConta1 = self.csocket.recv(1024).decode()
                c1 = cadConta.busca(recebeConta1)
                if c1 != None:
                    self.csocket.send('True'.encode())
                    recebeValor = self.csocket.recv(1024).decode()
                    if c.transfere(c1,float(recebeValor)):
                        #update dos saldo
                        cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeConta))
                        for info in cursor:
                            self.aux = info[0]
                        cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(str(c.saldo_conta()),info[0]))
                        #update dos saldo
                        cursor.execute('SELECT * from contas_banco WHERE numero = {}'.format(recebeConta1))
                        for info in cursor:
                            self.aux = info[0]
                        cursor.execute('UPDATE contas_banco SET saldo = {} WHERE id = {}'.format(str(c1.saldo_conta()),info[0]))
                        conexao.commit()
                        self.csocket.send('True'.encode())
                    else:
                        self.csocket.send('False'.encode())
                else:
                    self.csocket.send('False'.encode())
            else:
                self.csocket.send('False'.encode())




        
            

        
        #print("Client at ", ClientAddress, " disconnected...")



if (__name__ == '__main__' ):
    host = 'localhost'
    port = 8100
    addr = (host, port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)

    print("SERVIDOR INICIADO!")
    print("Aguardando nova conexao...")
    
    cad = Cadastro()
    cadConta = Cadastro_Conta()

    #alteracao do banco de dados
    conexao = mysql.connect(host = 'localhost', database = 'banco' ,user = 'root', password = 'paulo2008')
    cursor = conexao.cursor()
    server.listen(10)
    sql = """CREATE TABLE IF NOT EXISTS contas_banco(id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE, nome text NOT NULL, sobrenome text NOT NULL, cpf text NOT NULL, numero text NOT NULL,  saldo text NOT NULL,  limite text NOT NULL);"""

    cursor.execute(sql)

    cont = 0
    cursor.execute('SELECT * from contas_banco')

    aux = 0
    aux_id = 0
    print('Mostrando contas:\n')
    for info in cursor:
        print(info)
        p = Cliente(info[1],info[2],info[3])
        c = Conta(p,info[4],int(info[5]),info[6])
        cadConta.cadastra(c)
        aux_id = int(info[0])
        aux = int(info[4])
    
    aux_id+=1
    # cursor.execute('UPDATE contas_banco SET saldo = c.saldo WHERE id = 0')

    sinc = threading.Lock()
    numero = 0;
    while True:
        numero+=1
        Clientesock, ClientAddress = server.accept()
        newthread = ClienteThread(ClientAddress, Clientesock, numero, aux, aux_id, sinc)
        newthread.start()

                    

   

