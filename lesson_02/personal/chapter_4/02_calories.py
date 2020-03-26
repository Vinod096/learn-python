#Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
#uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

calories_burn_per_minute = 4.2
minutes = 0
for i in range (0,minutes + 1):
    minutes = int(input("enter number of minutes :"))
    calories_burn_per_minute = calories_burn_per_minute * minutes
print("calories burned :",calories_burn_per_minute)
