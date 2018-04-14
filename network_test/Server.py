import socket

NUM_CONNECTIONS = 5
PORT = 6112

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
print socket.gethostbyname(socket.gethostname())

s.bind((host, PORT))
s.listen(NUM_CONNECTIONS)

while True:
    c, addr = s.accept()
    print 'Got connectiong from', addr
    c.sendall('Connection accepted')
    data = c.recv(1024)
    print data
