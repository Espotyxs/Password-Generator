import random
import string
ras = random.randint(20,25)
pos = 0
rand = random.randint(1,3)
pss = str()
print("Password Generator, created by Xavier Sanchez (Espotyxs) 2024")
while ras >= pos:
    if rand == 1:
        pss = (random.choice(string.ascii_uppercase) + pss )
        pos = pos + 1
        rand = random.randint(1,3)
    elif rand == 2:
        pss = (random.choice(string.ascii_lowercase) + pss )
        pos = pos + 1
        rand = random.randint(1,3)
    else:
        pss = (random.choice(string.ascii_letters) + pss)
        pos = pos + 1
print("# Your password is")
print("#", pss)
print("# Here you go! {xD")