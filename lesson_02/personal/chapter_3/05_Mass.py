#Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
#the amount of mass of an object in kilograms, you can calculate its weight in newtons with
#the following formula:
#weight = mass * 9.8
#Write a program that asks the user to enter an object’s mass, and then calculates its weight.
#If the object weighs more than 500 newtons, display a message indicating that it is too
#heavy. If the object weighs less than 100 newtons, display a message indicating that it is
#too light.

mass = float(input("enter object's mass : "))
weight = mass * 9.8
print("weight :",weight)
if  weight >= 500:
    print("weight is too heavy")
elif weight <= 100:
    print("weight is less than 100 newtons")


