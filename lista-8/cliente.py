import socket

ip = 'localhost'
port = 8100

addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

while True:
    mensagem = input('Digite uma mensagem (caso digite ''sair'' a conexão e finalizada): ')
    client_socket.send(mensagem.encode())

    print('Mensagem enviada!!')
    aux = client_socket.recv(1024).decode()
    print(aux)

    if mensagem == 'Sair' or mensagem == 'sair':
        break

client_socket.close()