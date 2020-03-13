import time
import sys
import socket
import os

s = socket.socket()
host = "*Insert your ip adress here*"
port = 8080
s.connect((host, port))
print("")
print(" Connected to server ")

command = s.recv(1024)
command = command.decode()
if command == "txt":
    print("")
    print("Shutdown command")
    s.send("Command recieved".encode())
    os.system("test.txt")