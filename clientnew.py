import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 8888
def Check_PrimRoot(p,y):
    l=[]
    for i in range(1,p):
        ans=pow(y,i,p)
        if ans not in l:
            l.append(ans)
    if len(l)==p-1:
        return True
    else:
        return False
server_socket.bind((LOCALHOST,port))
server_socket.listen(6)
print("New Client started...")
client_sockets,addr=server_socket.accept()
p= int(input("Enter a prime number(p): "))
while(True):
    alpha= int(input("Enter primitive root of the prime number(alpha): "))
    if(Check_PrimRoot(p,alpha)):
        break
    else:
        print(alpha,"is not a primitive root of",p)
x= int(input("Enter Your private key(Xa): "))
ans=pow(alpha,x,p)
client_sockets.send(str(ans).encode())             
client_sockets.close()