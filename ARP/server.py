import socket

host= socket.gethostname()
port =5002

server= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip=['167.78.9.1','177.0.32.9']
mac=['8A:6B:AA:C2','9B:EE:B3:AA']
server.bind((host,port))

ind=9
data,adr = server.recvfrom(1024)
data = data.decode('utf-8')
for x in ip:
    # print(x,data)
    if x==data:
        ind=ip.index(x)
        break

if ind ==9:
    print('Not Found')
else:
    print(f"Mac Address :{mac[ind]} of Ip address {data}")

