import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 9990

s.connect((LOCALHOST,port))
print("New client created:")

def discreteLog(key,alpha,p):
    for i in range(p-1):
        if (pow(alpha,i,p)==key):
            return i
    return 0
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
       
            
while(True):
    print("\n****Diffie Helman Key Exchange****\n")
    print("1.KeyGeneration\n2.DiscreteLog\n3.Man in the middle\n4.Exit")
    choice=int(input("Enter Choice:"))
    s.send(str(choice).encode())
    if(choice==1):
        p= int(input("Enter a prime number(p): "))
        while(True):
            alpha= int(input("Enter primitive root of the prime number(alpha): "))
            if(Check_PrimRoot(p,alpha)):
                break
            else:
                print(alpha,"is not a primitive root of",p)
        x= int(input("Enter Your private key(Xa): "))
        ans=pow(alpha,x,p)
                
        s.send(str(p).encode())
        s.send(str(alpha).encode())
        s.send(str(ans).encode())
        pubkey=s.recv(1024).decode()
        print("Public Key of Bob(Yb):",pubkey)
        check=pow(int(pubkey),x,int(p))
        print("Checking Key:",check)
    elif (choice==2):
        p= int(input("Enter a prime number(p): "))
        alpha= int(input("Enter primitive root of the prime number(alpha):"))
        key=int(input("Enter Exchanged Key(Yb):"))
        x=discreteLog(key,alpha,p)
        if(x==0):
            print("Cannot Find Discrete log")
        else:
            print("Private Key of Bob:",x)
    
    elif(choice==3):
        port1=8888
        s1.connect((LOCALHOST,port1))     
        pubkey1=s1.recv(1024).decode()
        print("Public Key of User A",pubkey1)
        s1.close()
        pubkey2=s.recv(1024).decode()
        print("Public Key of User B:",pubkey2)
    elif(choice==4):
        break
        
s.close()