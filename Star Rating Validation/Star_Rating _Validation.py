star_rating = int(input("Enter a star rating between 0 and 5: "))

while star_rating < 0 or star_rating > 5:
    print("Invalid star rating. Try again!")
    star_rating = int(input("Enter a star rating between 0 and 5: "))
    
print("Thank you!")
   