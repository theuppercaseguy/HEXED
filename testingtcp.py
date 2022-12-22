import socket

HOST = '192.168.137.15' # Server IP or Hostname
PORT = 1234 # Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
print(socket.gethostname())

s.bind((HOST, 1234))

s.listen(5)
print('Socket awaiting messages')
(conn, addr) = s.accept()
conn.close()
print('Connected')

# awaiting for message
while True:
	data = conn.recv(1024)
	print ('I sent a message back in response to: ' + data)
	
	if data == 'quit':
		conn.send('Terminating')
		break
	else:
		reply = 'Unknown command'

	# Sending reply
	# conn.send(reply)

conn.close() # Close connections