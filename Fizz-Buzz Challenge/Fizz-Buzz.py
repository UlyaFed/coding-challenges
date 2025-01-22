num = 0
for num in range(100):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 5 == 0 and num % 3 == 0:
        print("Fizz-buzz")
    else:
        print(num)