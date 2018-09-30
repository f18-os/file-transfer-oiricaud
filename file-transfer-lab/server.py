import os
import socket
HOST = '0.0.0.0'
PORT = 5000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))

socket.listen(1)
while 1:
    conn, addr = socket.accept()
    print('New client connected ..')

    reqCommand = conn.recv(1024)
    print('reqCommand  -->' , reqCommand)
    print('Client> %s' % reqCommand)
    if reqCommand == 'quit':
        break
    else:
        temp = reqCommand.decode("utf-8")
        string = temp.split(' ', 1)
        reqFile = 'serverFiles/' + string[1]
        head, sep, tail = reqFile.partition('.txt')
        file_name = head + '.txt'
        size_of_file = os.stat('testFile2.txt').st_size
        block_rate = size_of_file / 1000
        print('block_rate', block_rate)
        if string[0] == 'put':
            curr_block = 0
            with open(file_name, 'wb') as file_to_write:
                while True:
                    print("current block --> ", curr_block)
                    if curr_block > block_rate:
                        file_to_write.close()
                        break
                    else:
                        curr_block = curr_block + 1
                        data = conn.recv(1024)

                        print("data ----> ", data)
                        file_to_write.write(data)

            print('Receive Successful')
        elif string[0] == 'get':
            with open(reqFile, 'rb') as file_to_send:
                for data in file_to_send:
                    conn.sendall(data)
            print('Send Successful')
    conn.close()

socket.close()
