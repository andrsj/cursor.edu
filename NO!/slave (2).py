import time
import sys
import socket
import os

s = socket.socket()
host = "192.168.5.105"
port = 8080
s.connect((host, port))
print("")
print(" Connected to server ")
while True:
    command = s.recv(1024)
    command = command.decode()
    if command == "txt":
        print("")
        print("Shutdown command")
        s.send("Command recieved".encode())
        f = open("guru99.txt", "w+")
    if command == "txt1":
        print("")
        print("Shutdown command")
        s.send("Command recieved".encode())
        f = open("gur.txt", "w+")