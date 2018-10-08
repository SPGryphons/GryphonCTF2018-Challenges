#! /usr/bin/env python3
import socket
PORT=30152
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('0.0.0.0',PORT))
c=client.recv(256)
print(c.decode())
client.sendall("n".encode())
while 1:
	c=client.recv(256).decode().strip()
	print(c)
	client.sendall(str(c).encode())
