# creating the client
import socket

c = socket.socket()
# connecting to the server

c.connect(("localhost",9999))
# sending the data to the server

name = input("Enter your name: ")
c.send(bytes(name, "utf-8"))
# c.accept()
print(c.recv(1024).decode())