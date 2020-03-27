#Write a program that calculates the amount of money a person would earn over a period
#of time if his or her salary is one penny the first day, two pennies the second day, and
#continues to double each day. The program should ask the user for the number of days.
#Display a table showing what the salary was for each day, and then show the total pay at
#the end of the period. The output should be displayed in a dollar amount, not the number
#of pennies.

number_of_days = int(input("enter number of days : "))
earnings_per_day = float(input("enter earning per day : "))
total_pennies = 0
for i in range (1,number_of_days + 1):
    total_pennies = total_pennies + earnings_per_day
    print(f"earnings per {i} day : {total_pennies} ")
total = total_pennies * 0.01
print("you've $:",total,"pennies")
