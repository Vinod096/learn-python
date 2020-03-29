#Write a program with a loop that asks the user to enter a series of positive numbers. The
#user should enter a negative number to signal the end of the series. After all the positive
#numbers have been entered, the program should display their sum.

total = 0
number = int(input("enter a positive number :"))
while number > -1 :
    total = total + number
    number = int(input("enter a positive number or negative number to end :"))
print("total of postive numbers :",total)



