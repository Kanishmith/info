import hashlib
alphabets="abcdefghijklmnopqrstuvwxyz"
l=[]
for i in alphabets:
    for j in alphabets:
        l.append(i+j)
d={}
for i in l:
    d[i]=hashlib.sha256(i.encode()).hexdigest()
print(d)
key_list = list(d.keys())
value_list = list(d.values())
while(True):
    print("1.Convert Password to key\n2.Dictionary Attack\n3.Exit")
    choice=int(input("Enter You Choice: "))
    if (choice==1):
        passwd=input("Enter Password: ")
        print(d[passwd])
    elif (choice==2):
        hashvalue=input("Enter Hash Value: ")
        pos = value_list.index(hashvalue)
        print(key_list[pos])
    elif (choice==3):
         break