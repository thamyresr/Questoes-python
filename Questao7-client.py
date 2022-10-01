import socket, pickle

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.settimeout(5)
destino = (socket.gethostname(), 4000)
msg = ''
socket_cliente.sendto(msg.encode('utf8'), destino)

for i in range(5):
    socket_cliente.sendto(msg.encode('utf8'), destino)
    try:
        bytes = socket_cliente.recv(1024)
        lista = pickle.loads(bytes)

        print('Memory information:')
        print('{:>8}'.format('Total') + '{:>8}'.format('Free'))
        for j in lista:
            print('{:>8}'.format(j), end=' ')

        msg = 'fim'
        socket_cliente.sendto(msg.encode('utf8'), destino)
        break
    except socket.timeout as error:
        print(str(error))

input('\n Press any key to close the program...')