import socket, os, pickle

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
PORT = 5001
socket_server.bind((host, PORT))
socket_server.listen()
print('Server name:', host, 'waiting for connection on port', PORT)

run = True
while run:
    (socket_cliente, addr) = socket_server.accept()
    print("Connected to:", str(addr))
    msg = socket_cliente.recv(4096)
    diretory = msg.decode('utf8')
    if os.path.isdir(diretory):
        socket_cliente.send('1'.encode('utf8'))
        list_directories = os.listdir(diretory)
        files_list = []
        for i in list_directories:
            path = os.path.join(diretory, i)
            if os.path.isfile(path):
                files_list.append(i)
        bytes_resp = pickle.dumps(files_list)
        socket_cliente.send(bytes_resp)
        msg = socket_cliente.recv(4096)
    else:
        print("File not found")
        socket_cliente.send('-1'.encode('utf8'))
        exit()
    if str(msg.decode('utf8')) == 'fim':
        print('Program closed!')
        socket_cliente.close()
        socket_server.close()
        run = False
        exit()