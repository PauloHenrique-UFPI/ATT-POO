'''
    DESCRIPTION
        arquivo do cliente que envia informações para o servidor
        class: Cliente_connect
'''
import socket

class Cliente_connect:
    def connect(self):
        '''
            Modulo que conecta o cliente ao servidor
                :param ip: str
                    valor do tipo string
                :param port: int
                    valor do tipo inteiro
                :param add: dupla
                    valor do tipo string e inteiro
        '''
        ip = 'localhost'
        port = 8100
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

    def passa_mensagem(self, frase):
        '''
            Modulo que envia e recebe informacoes ao servidor
                :param aux: str
                    valor do tipo string
        '''
        self.client_socket.send(frase.encode())
        print('Mensagem enviada')
        aux = self.client_socket.recv(1024).decode()
        return aux
    
      
        
