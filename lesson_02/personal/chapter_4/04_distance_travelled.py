#The distance a vehicle travels can be calculated as follows:
#distance = speed * time
#For example, if a train travels 40 miles per hour for three hours, the distance traveled is
#120 miles. Write a program that asks the user for the speed of a vehicle(in miles per hour)
#and the number of hours it has traveled. It should then use a loop to display the distance
#the vehicle has traveled for each hour of that time period. Here is an example of the desired
#output:
#What is the speed of the vehicle in mph? 40 e
#How many hours has it traveled? 3 e
#Hour Distance Traveled
#1               40
#2               80
#3               120

speed = 0
hours = 0
speed = int(input("enter miles travelled : "))
hours = int(float(input("Enter number of hours :")))
print("********************")
print("hours"  '\t' "speed"  '\t' "miles")
print("********************")
for hours in range (1,hours + 1):
    distance = speed * hours
    print(hours,'\t',speed,'\t',distance,"miles")
