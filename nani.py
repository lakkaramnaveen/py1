import socket
# it's establishing a connection between two parties, similar to making a call over the phone
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org',80))
# it's like set of guildlines or rules to follow
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_sock.send(cmd)

while True:
    data = my_sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

my_sock.close()