#Design a program that lets the user enter the total rainfall for each of 12 months into a
#list. The program should calculate and display the total rainfall for the year, the average
#monthly rainfall, and the months with the highest and lowest amounts.

rainfall_in_a_year = []
for i in range (1,13):
    rainfall_in_each_month = float(str(input(f"Enter month {i} rainfall :")))
    rainfall_in_a_year.append(rainfall_in_each_month)
total = sum(rainfall_in_a_year)
print("total rainfall in a year :",total)
average = total / len(rainfall_in_a_year)
print("average rainfall in a year is :",average)
print("Maximum rainfall in a year :",max(rainfall_in_a_year))
print("Minimum rainfall in a year :",min(rainfall_in_a_year))
