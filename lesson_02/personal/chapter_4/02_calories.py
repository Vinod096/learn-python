#Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
#uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

calories_burn_per_minute = 4.2
minutes = 0
for i in range (10,31,5):
#    minutes = int(input("enter number of minutes :"))
    result = calories_burn_per_minute * i
    print(f"calories burned after {i}  mins:{result}")
