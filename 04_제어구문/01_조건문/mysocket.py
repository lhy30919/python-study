import socket

s=socket.socket()

ip = "192.168.10.60"
port=21

s.connect((ip,port))

ans=s.recv(1024)

print(ans)