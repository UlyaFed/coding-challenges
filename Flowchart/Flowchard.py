import random

die1 = random.randint(1,6) 
die2 = random.randint(1,6) 
die3 = random.randint(1,6) 

print("Die1 is", die1)
print("Die2 is", die2)
print("Die3 is", die3)

if die1 == die2 == die3:
    print("Three of a kind!!!")
elif die1 == die2 or die2 == die3 or die1 == die3:
    print("One pair!!!")
else:
    print("Better luck next time!")
    