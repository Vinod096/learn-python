#Design a program that asks the user to enter a store’s sales for each day of the week. The
#amounts should be stored in a list. Use a loop to calculate the total sales for the week and
#display the result.

number_of_days = 7
sales = [0] * number_of_days
index = 0
total = 0
print("Enter each day sales :")
while index < number_of_days:
    print('Day #',index + 1,':', sep = '', end = '')
    sales[index] = float(input())
    index += 1
for value in sales:
    total += value
print("Total sales are :",total)

