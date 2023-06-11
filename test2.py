import socket

HOST = 'localhost'  # The remote host
PORT = 12345  # The same port as used by the server

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((HOST, PORT))
print('Connected to', HOST, 'on port', PORT)

# send and receive messages
while True:
    message = input('Enter message: ')
    s.sendall(message.encode())
    data = s.recv(1024)
    if not data: break
    print('Received message:', data.decode())

# close the connection
s.close()