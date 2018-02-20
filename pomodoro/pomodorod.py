import os
import sys
import socket
from datetime import datetime, timedelta

if os.fork():
    sys.exit()

socket_address = "/tmp/pomodoro.sock"

if os.path.exists(socket_address):
    os.remove(socket_address)

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(socket_address)

server.listen()

time_up = None
mode = 5

while True:
    connection, ignored = server.accept()
    data = connection.recv(1024)
    command = data.decode('utf-8')

    if command == "toggle":
        mode = 30 - mode # 25 -> 5, 5 -> 25
        time_up = datetime.now() + timedelta(seconds = mode * 60)
        connection.sendall("Timer has been toggled.".encode('utf-8'))
    elif command == "reset":
        mode = 5
        time_up = None
        connection.sendall("Timer has been reset.".encode('utf-8'))
    elif command == "left" and time_up is not None:
        seconds_left = max((time_up - datetime.now()).total_seconds(), 0)
        minutes_left = int(seconds_left / 60)
        seconds_left = int(seconds_left) % 60
        left = "{:0>2}".format(minutes_left) + ":" + "{:0>2}".format(seconds_left)
        connection.sendall(str(left).encode('utf-8'))
    elif command == "left":
        connection.sendall("25:00".encode('utf-8'))
    elif command == "shutdown":
        connection.close()
        break
    else:
        connection.sendall("Unknown command.".encode('utf-8'))
        
    connection.close()

server.close()
os.remove(socket_address)
