import socket

ISHOST = false
PORT = 6112

if ISHOST:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    print 'Host on: ' + host
    
    soc.bind((host, port))
    soc.listen(5)
endif
