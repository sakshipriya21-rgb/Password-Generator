import random
import string 
char=string.ascii_letters+string.digits+string.punctuation
passLength=int(input("Enter the length of your required password : "))
password=""
for val in range(passLength):
    password+=random.choice(char)
print("Your random password is ",password)