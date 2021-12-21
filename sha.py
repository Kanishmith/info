def boolean(B,C,D):
	return(hex((B&C)|(~B&D)))

def summation(x,y):
	z=hex(x+y)
	z='0x'+z[-8:]
	return(z)

def shift(x,n):
	x=bin(x)[2:]
	x='0'*(32-len(x))+x
	print(x)
	z=hex(int(x[n:]+x[:n],2))
	return(z)

if __name__ == "__main__":
	A =int('0x00000000',16)
	B =int('0x11111111',16)
	C =int('0X22222222',16)
	D =int('0X33333333',16)
	E =int('0X44444444',16)
	l=""
	r='0x5A827999'
	word=input("Enter the plain text:")
	for i in word:
		l+=hex(ord(i))[2:]
	k=summation(E,int(boolean(B,C,D),16))
	print(k)
	k=summation(int(k,16),int(shift(A,5),16)) 
	k=summation(int(k,16),int(l,16))
	k=summation(int(k,16),int(r,16))
	E=hex(D)
	D=hex(C)
	C=shift(B,30)
	B=hex(A)
	A=k
	print("The hash generated after one round of SHA-1 is:\n",A,B,C,D,E)