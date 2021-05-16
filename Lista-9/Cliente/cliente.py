import socket

class Cliente_connect:
      

    def connect(self):
        ip = 'localhost'
        port = 8100
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

    def passa_mensagem(self, frase):
        self.client_socket.send(frase.encode())
        print('Mensagem enviada')
        aux = self.client_socket.recv(1024).decode()
        return aux
    
      
        
