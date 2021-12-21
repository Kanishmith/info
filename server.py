import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 9990

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
server_socket.listen(5)

print("Server started...")

client_sockets,addr=server_socket.accept()
c = client_sockets.recv(1024).decode()

p = client_sockets.recv(1024).decode()
alpha = client_sockets.recv(1024).decode()
pubkey=client_sockets.recv(1024).decode()
print("Prime(p) is:",p)
print("Primitive Root(alpha) is",alpha)
x1= int(input("Enter Your private key(Xb): "))
print("Public Key of Alice(Ya):",pubkey)
ans=pow(int(alpha),x1,int(p))
client_sockets.send(str(ans).encode())
check=pow(int(pubkey),x1,int(p))
print("Checking Key:",check)
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