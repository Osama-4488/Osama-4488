import secrets
import string

le = string.ascii_letters
digit = string.digits
special_chars = string.punctuation
alphabet = le + digit + special_chars
pwd_length = 5
pwd = ''
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))
print(pwd)
while True:
    pwd =''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))
    
    if (any(char in special_chars for char in pwd ) and
    sum(char in digit for char in pwd )>=2):
            break
        
print(pwd)