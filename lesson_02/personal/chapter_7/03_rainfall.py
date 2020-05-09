#Design a program that lets the user enter the total rainfall for each of 12 months into a
#list. The program should calculate and display the total rainfall for the year, the average
#monthly rainfall, and the months with the highest and lowest amounts.

total_months = 12
rainfall_in_each_month = [0] * 12
#print(rainfall_in_each_month)
index = 0
total = 0
while index < total_months:
    print('month -- ', index + 1, ':', sep='', end='')
    rainfall_in_each_month[index] = float(input())
    index += 1
for Value in rainfall_in_each_month:
    total += Value
print("total rainfall in a year is :",total)
average = total / len(rainfall_in_each_month)
print("average rainfall in a year is :",average)
print("Maximum rainfall in a year :",max(rainfall_in_each_month))
print("Minimum rainfall in a year :",min(rainfall_in_each_month))