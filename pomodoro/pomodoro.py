import socket
import os
import sys

socket_address = '/tmp/pomodoro.sock'

if os.path.exists(socket_address):
    socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    socket.connect(socket_address)
    socket.sendall(sys.argv[1].encode('utf-8'))
    response = socket.recv(1024)
    print(response.decode('utf-8'))
    socket.close()
else:
    print('Server not running.')
    sys.exit(1)
