import socket

host = 'localhost'
port = 8100
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)

print('Aguardando conexao...')

con, cliente = serv_socket.accept()
print('Concctado')
print('Aguardando mensagem...')

while True:
    recebe = con.recv(1024)
    con.send('teste'.encode())

    print('mensagem recebida: '+ recebe.decode())
    if recebe.decode() == 'sair' or recebe.decode() == 'Sair':
        break

serv_socket.close()