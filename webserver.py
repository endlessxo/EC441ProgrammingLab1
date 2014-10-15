import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 84)
print sys.stderr, 'Starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def find_start(arga):
	for i in range (0, len(arga)):
		if arga[i] == '/':
			return i+1
	return 0

def find_end(arga):
	for i in range (0, len(arga)):
		if arga[i:i+4] == 'html':
			return i+4
	return 0

while True:
    print 'Ready to serve...'
    connection, client_address = sock.accept()
    try:
    	message = connection.recv(20)
    	message = message[find_start(message):find_end(message)]
    	filename = message
	
    	# f = open(filename, 'r')
    	# read_data = f.read()
    	# print '200 Found'
    	# print read_data

    	print '200 Found'
    	print open(filename, 'r').read()
		

        # # Receive the data in small chunks and retransmit it
        # while True:
        #     data = connection.recv(1000)
        #     # print sys.stderr, 'received "%s"' % data
        #     if data:
        #         print sys.stderr, 'sending data back to the client'
        #         connection.sendall(data)
        #     else:
        #         print sys.stderr, 'no more data from', client_address
        #         break
    except:
    	print '404 Not Found'        
    finally:
        # Clean up the connection
        connection.close()

