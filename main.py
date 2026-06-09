import random
import string 
char=string.ascii_letters+string.digits+string.punctuation
passLength=random.randint(4,8) # including 4 and 8
password=""
for val in range(passLength):
    password+=random.choice(char)
print("Your random password is ",password," of length ",passLength)