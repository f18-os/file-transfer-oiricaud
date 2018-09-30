import os
import socket
import sys

HOST = '0.0.0.0'  # server name goes in here
PORT = 5000


def put(command_name):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    temp = command_name.encode("utf-8")
    socket1.send(temp)
    string = command_name.split(' ', 1)
    input_file = string[1]
    print('SIZE', os.stat(input_file).st_size)
    with open(input_file, 'rb') as file_to_send:
        for data in file_to_send:
            socket1.sendall(data)
    print('PUT Successful')
    socket1.close()
    return


def get(command_name):
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((HOST, PORT))
    temp = command_name.encode("utf-8")
    socket1.send(temp)
    string = command_name.split(' ', 1)
    input_file = string[1]
    print('SIZE', os.stat(input_file).st_size)
    with open(input_file, 'wb') as file_to_write:
        while True:
            data = socket1.recv(1024)
            # print data
            if not data:
                break
            # print data
            file_to_write.write(data)
    file_to_write.close()
    print('GET Successful')
    socket1.close()
    return


while 1:
    print('Help')
    print('"put [filename]" to send the file the server ')
    print('"get [filename]" to download the file from the server ')
    print('"quit" to exit')
    inputCommand = sys.stdin.readline().strip()
    if inputCommand == 'quit':
        sys.exit(1)
    else:
        string = inputCommand.split(' ', 1)
        if string[0] == 'put':
            put(inputCommand)
        elif string[0] == 'get':
            get(inputCommand)
