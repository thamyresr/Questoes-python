import socket, pickle

def print_list(list):
    for i in list:
        print(i)

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
directory_path = input('Enter with directory path: ')

try:
    socket_client.connect((socket.gethostname(), 5001))
    socket_client.send(directory_path.encode('utf8'))
    message = socket_client.recv(4096)
    if message.decode('utf8') == '1':
        bytes = socket_client.recv(4096)
        files_list = pickle.loads(bytes)
        print_list(files_list)
        msg = 'fim'
        socket_client.send(msg.encode('utf8'))
    else:
        print("Directory", '\'' + directory_path + '\'', "does not exist.")
except socket.error as error:
    print(str(error))
socket_client.close()

input('Press any key to close the program...')