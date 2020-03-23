#Create a change-counting game that gets the user to enter the number of coins required
#to make exactly one dollar. The program should prompt the user to enter the number of
#pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one
#dollar, the program should congratulate the user for winning the game. Otherwise, the
#program should display a message indicating whether the amount entered was more than
#or less than one dollar.

one_penny = 1
one_nickle = 5
one_dime = 10
one_quarter = 25
one_dollar = 100
pennies_having = int(input("enter number of pennies :"))
total_pennies = one_penny * pennies_having
print("total pennies :",total_pennies)
nickels_having = int(input("enter number of nickles :"))
total_nickles = one_nickle * nickels_having
print("total nickles :",total_nickles)
dimes_having = int(input("enter number of dimes :"))
total_dimes = one_dime * dimes_having
print("total dimes :", total_dimes)
quarters_having = int(input("enter number of quarters :"))
total_quarters = one_quarter * quarters_having
print("total quarters :", total_quarters)
total_value_of_coins = total_pennies + total_nickles + total_dimes + total_quarters
print("total values of all coins :",total_value_of_coins)
if total_value_of_coins == one_dollar:
    print("congrats for winning")
elif total_value_of_coins <= one_dollar or total_value_of_coins >= one_dollar:
    print("coins are more than one dollar")
else:
    print("coins are less than one dollar")
