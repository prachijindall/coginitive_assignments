import random
import string
def password(length):
    chara=string.ascii_letters + string.digits + string.punctuation
    passs=''.join(random.choice(chara) for i in range(length))
    return passs
length=int(input("enter"))
passs=password(length)
print(passs)
    