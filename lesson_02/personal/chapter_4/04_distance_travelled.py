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

distance_travelled = int(input("enter miles travelled : "))
hours_travelled = int(input("Enter number of hours :"))
for hours in range (1,hours_travelled):
    distance = distance_travelled * hours_travelled
print("In",hours_travelled,"hours,you've travelled",distance,"miles")