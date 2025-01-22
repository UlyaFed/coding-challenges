price = int(input("Enter the price of your item: "))
discount_rate = int(input("Enter the percentage discount: "))
discount = price * discount_rate / 100
new_price = price - discount

print(f"Price before discount: {price}, discount: {discount_rate}, new price is {new_price}")

 