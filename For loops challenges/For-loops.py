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


