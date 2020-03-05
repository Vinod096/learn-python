price_for_food = float(input("please enter the amount : "))
tip = 0.18 * price_for_food
print("tip is : ",tip)
tax = 0.07 * price_for_food
print("tax on food is : ",tax)
total = tip + tax + price_for_food
print("total amount with taxes is : ",total)
