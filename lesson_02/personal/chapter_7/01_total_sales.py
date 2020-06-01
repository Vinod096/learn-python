#Design a program that asks the user to enter a store’s sales for each day of the week. The
#amounts should be stored in a list. Use a loop to calculate the total sales for the week and
#display the result.

everyday_sales = []
for i in range (1,8):
    number_of_sales = int(input(f"Enter day {i} : "))
    everyday_sales.append(number_of_sales)
total = sum(everyday_sales)
print("Total sales in a week :",total)