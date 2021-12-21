def check_prime(a):
    for i in range(2,a):
        g=0
        if a%i==1:
           g=1
           return g
        else:
            break

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def encryption(n,e):
    text=[]
    l=[]
    h=input("Enter the message : ").lower()
    for i in h:
        text.append(i)

    alpha=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for i in range(len(text)):
        if text[i] in alpha:
            c=((alpha.index(text[i]))**e)%n        
            l.append(c)

    for i in range(len(l)):
        print("Key ",i,": ",l[i])

def evaluate(n,fi,ch):
    e=int(input("Enter value of E : "))
    if gcd(e,fi)==1:
        print("ok ... Good to go !")
        if ch==0:
            encryption(n,e)
        elif ch==1:
            d=int(input("Enter value of generated key D : "))
            decrypt(n,d)
        
    else:
        print("Cannot be Done :(")


def extended(e,fi):
    a,b=max(e,fi),min(e,fi)
    t1=0
    t2=1
    y=0
    while b!=0:
        r=a%b
        q=a//b
        t=t1-q*(t2)
        t1,t2=t2,t
        a,b=b,r
    if t1<0:
        y=t1+t2
        return y
    elif t2>0:
        y=t2
        return y

def keygen(n,fi):
    e=int(input("Enter public key value (E): "))
    y=extended(e,fi)
    d=y%fi
    print("Key generated is : ",d)    

def decrypt(n,d):
    l2=[]
    l3=[]
    for i in range(5):
        c=int(input("Enter encrypted keys : "))
        l2.append(c)
    for i in l2:
        m=pow(i,d,n)
        l3.append(m)
    alpha=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    s=""
    for i in l3:
        s+=alpha[i]
    print(s)


def body(b,n,fi):
    b=b
    if b==1:
        evaluate(n,fi,0)
    elif b==2:
        evaluate(n,fi,1)


print("Enter Your choice:")

while True:
    o=int(input("1.Key Generation\t2.Encryption\t3.Decryption\t3.Exit\n"))
    if o==1:
        p=int(input("Enter a prime number : "))
        q=int(input("Enter another prime number : "))
        if check_prime(p) == 1 and check_prime(q)==1:
            print("Both are Prime.")
            n=p*q
            fi=(p-1)*(q-1)
            keygen(n,fi)
    elif o==2:
        body(1,n,fi)
    elif o==3:
        body(2,n,fi)
    elif o==4:
        quit()