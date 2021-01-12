#Socket Programming - Bharath Mukka
#LAB 2B, Computer Networking
import socket module
from socket import *

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM) 

serverPort = 12005
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print ("addr:\n", addr)
	try:
		message = connectionSocket.recv(1024) 
		print("message: \n", message)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read() 
		print("outputdata:", outputdata)
		#now = datetime.datetime.now()
		#Sending one HTTP header line into socket
		first_header = "HTTP/1.1 200 OK \n"
		print("first_header:", first_header)
		connectionSocket.send(bytes(first_header))
		#Send content of response of requested file to the client  
		for i in range(0, len(outputdata)):
			connectionSocket.send(bytes(outputdata[i]))
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>"))
		#Close client socket 
		connectionSocket.close()
serverSocket.close()
