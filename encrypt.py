#Simple encryption message

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)  
key = chars.copy()
random.shuffle(key)

#Encrypt Message
plainText = input("Enter message you want to encrypt: ")
cipherText = ""

for char in plainText:
    index = chars.index(char)
    cipherText += key[index]
    
print(f"original  text: {plainText}")
print(f"encrypted text: {cipherText}")
    
#Decrypt Message
cipherText = input("Enter message you want to decrypt: ")
plainText = ""

for char in cipherText:
    index = key.index(char)
    plainText += chars[index]

    
print(f"enrypted text: {cipherText}")
print(f"original text: {plainText}")
    
    

print(f"chars: {chars}")
print(f"key  : {key}")