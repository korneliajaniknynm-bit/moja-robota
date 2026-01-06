import random

znaki = " +-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "
print("hej! utworzymy tobie dzis hasło!")

l = int(input("Jak długie ma być hasło(numer liczb)?"))

h = ""
for i in range(l):
    h = h + random.choice(znaki)
    
print("oto twoje nowe hasło: ", h)
print("cześć wszystkim")
