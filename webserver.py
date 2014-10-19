import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 80)

print "Starting up %s port %s" % address

serverSocket.bind(address)
serverSocket.listen(1)

while True:
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept()
	try:
		connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n')
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:], 'r').read()
		for i in range (0, len(f)):
			connectionSocket.send(f[i])
		connectionSocket.close()
	except:
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n\r\n')
		connectionSocket.close()
		