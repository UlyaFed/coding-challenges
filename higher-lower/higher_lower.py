from random import randint

num = randint(1,100)
guess = int(input("Guess a number: "))

while guess != num:
    
    if guess < num:
        print("Higher!")
    elif guess > num:
        print("Lower!")
    guess = int(input("Guess a number: "))
    
else:
    print("You win!") 
        