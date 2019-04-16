#6.password_gen.py
import random
import string

string.ascii_lowercase
string.digits
string.punctuation

characters = string.ascii_lowercase + string.digits + string.punctuation

pwlength = int(input("How many characters in this password? > "))

for num in range (pwlength):
    pwlength = random.choice(characters)
    print(pwlength)
