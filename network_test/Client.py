import socket

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
address = socket.gethostbyname(socket.gethostname())
server_port = 6112

s.connect((address, server_port))
s.sendall('This is the client')
data = s.recv(1024)
print data
