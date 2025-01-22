#First task. Writing lines.
text = "I will listen to my teacher and complete my work on time."

for i in range(10):
    print(text)
    
# Second task. Count in 5 from 0 to 500.

num = 0
for i in range(505):
    if num % 5 == 0:
        print (num)
    num = num + 1
        
# Third task. Count down from 100 to 0.

num = 100

while num >= 0:
    print(num)
    num = num - 1

# 4th task. The program starts by asking for a number. It will then display the times table for this given number.
num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

# 5th task. Recite the 26 letters of the Alphabet from A to Z.
letter = chr(65)
while ord(letter) <= 90:
    print(letter)
    letter = chr(ord(letter)+ 1)

# 6th task. Ask for a positive integer value and calculate the iterative sum for this given number.

num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer")
else:
    sum = 0
    
    for i in range(1, num + 1):
        sum += i
        
print(f"Iterative Sum for {num} is {sum}")

# 7th task. To calculate a factorial of a number! Your program will ask for the user to enter a positive integer value and return its factorial value.
num = int(input("Enter a positive integer: "))

if num <= 0:
    print("Please enter a positive integer")
else:
    factorial = 1
    
    for i in range(1, num + 1):
        factorial *= i
        
print(f"The factorial of {num} is {factorial}")