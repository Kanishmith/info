def encrypt(plaintext,key):
    plaintext = plaintext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in plaintext:
        if i in alpha:
            index = (alpha.find(i)+key) % len(alpha)
            result += alpha[index]
    return result.lower()
def decrypt(ciphertext,key):
    ciphertext = ciphertext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in ciphertext:
        if i in alpha:
            index = (alpha.find(i)-key) % len(alpha)
            result += alpha[index]
    return result.lower()
def bruteForce(ciphertext):
    ciphertext = ciphertext.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXY"
    for i in range(0,26):
        result = ""
        for j in ciphertext:
            if j in alpha:
                index = (alpha.find(j)-i) % len(alpha)
                result += alpha[index]
        print("#key",i,"=",result.lower())
def most(ciphertext):
    l = []
    max = 0
    ch = ''
    for i in ciphertext:
        if i not in l:
            l.append(i)
            if max < ciphertext.count(i):
                max = ciphertext.count(i)
                ch = i
    return ch
def frequencyAnalysis(ciphertext):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mo = most(ciphertext)
    print("Most occured",mo)
    l = ['e','t','a','o','i']
    for i in l:
        key = (alpha.find(mo) - alpha.find(i)) % 26
        if key < 0 :
            key+=26
        print("Key",key)
        print("Decrypted cipher text:", decrypt(ciphertext,key))
        choice = input("Enter the choice (y/n) ")
        if choice == 'y':
            continue
        else:
            break
if __name__  ==  "__main__":
    plaintext = input("Enter the message")
    key = int(input("Enter the key"))
    print("Encryption....")
    ciphertext = encrypt(plaintext,key)
    print("Cipher text is",ciphertext)
    print("Decryption....")
    plaintext = decrypt(ciphertext,key)
    print("Plaintext is",plaintext)
    print("Brute-Force attack....")
    bruteForce(ciphertext)
    print("Frequency analysis-attack...")
    frequencyAnalysis(ciphertext)