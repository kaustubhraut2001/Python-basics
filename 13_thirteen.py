# Zip function

names = ("A" , "b" , "c")
ages = (1, 2, 3)

c =	tuple(zip(names , ages))
print(c)


# Socket

import socket


s = socket.socket() # we can pass two parameters socket.AF_INET, socket.SOCK_STREAM
print("Socket created")
s.bind(('localhost', 9999)) #ip and port


# we needs to listern the clien and also specift the number of client
s.listen(3)
print("Waiting for connections")

# client will send the request
while True:
	c, address = s.accept()
	print("Got connection")
	data = c.recv(1024).decode() #dara that we are recveing from the client
	print(address , data)
	c.send(bytes(f"Welcome to the serve Testin Sockets in python {address} and data is {data}", "utf-8")) # data that we are sen ing back to gthe server it will recive all these data
	c.close()

