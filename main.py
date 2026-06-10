import random
import string 
char=string.ascii_letters+string.digits+string.punctuation
usage=input("Write 'G' for generating a password OR Write 'C' for checking the strength of your password : ")
if (usage=="C" or usage=="c"):
    checkPass=input("Enter your password :")
    uppercase=lowercase=digit=symbol=False
    for val in checkPass:
        if not uppercase:
            uppercase=val.isupper()
        if not lowercase:
            lowercase=val.islower()
        if not digit:
            digit=val.isdigit()
        if not symbol:
            if val in string.punctuation:
                symbol=True
    if(uppercase and lowercase and digit and symbol):
        print("Your password is STRONG ENOUGH!")
    else:
        print("You need a stronger password.")
elif (usage=="G" or usage=="g"):
    passLength=int(input("Enter the length of your password (greater than or equal to 4) :"))
    if passLength<4:
        print("Invalid length!")
    else:
        password=random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
        for val in range(passLength-4):
            password+=random.choice(char)
        print("Your random password is ",password)
else:
    print("Invalid Choice!")
