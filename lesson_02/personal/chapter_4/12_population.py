#Write a program that predicts the approximate size of a population of organisms. The
#application should use text boxes to allow the user to enter the starting number of organisms,
#the average daily population increase(as a percentage), and the number of days the
#organisms will be left to multiply. For example, assume the user enters the following values:
#Starting number of organisms: 2
#Average daily increase: 30%
#Number of days to multiply: 10
#The program should display the following table of data:
#Day Approximate Population
#1       2
#2       2.6
#3       3.38
#4       4.394
#5       5.7122
#6       7.42586
#7       9.653619
#8       12.5497
#9       16.31462
#10      21.209

size = 0
Starting_number_of_organisms = int(input("Starting_number_of_organisms : "))
daily_increase = int(input("daily increase : "))
Average_daily_increase = daily_increase / 100
print("Average daily increase :",Average_daily_increase)
number_of_days_to_multiply = int(input("number_of_days_to_multiply : "))
print("Day Approximate  Population :")
for number_of_days_to_multiply in range (1,number_of_days_to_multiply + 1):
    Starting_number_of_organisms = (Starting_number_of_organisms * Average_daily_increase) + Starting_number_of_organisms
    print(f"{number_of_days_to_multiply}   {Starting_number_of_organisms}")

