import socket, psutil, pickle

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
PORT = 4000
socket_servidor.bind((host, PORT))
print('Server name:', host, 'waiting for connection on port', PORT)

while True:
    (msg, client) = socket_servidor.recvfrom(1024)
    print(client)
    if msg.decode('utf8') == 'fim':
        break
    resp_list = []
    info_memory = psutil.virtual_memory()
    memory_total = round(info_memory.total / (1024 * 1024 * 1024), 2)
    free_memory = round(info_memory.free / (1024 * 1024 * 1024), 2)
    resp_list.append(str(memory_total) + 'GB')
    resp_list.append(str(free_memory) + 'GB')
    bytes_resp = pickle.dumps(resp_list)
    socket_servidor.sendto(bytes_resp, client)

socket_servidor.close()
