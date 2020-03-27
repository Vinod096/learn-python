#In mathematics, the notation n! represents the factorial of the nonnegative integer n . The
#factorial of n is the product of all the nonnegative integers from 1 to n. For example,
#7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5040
#and
#4! = 1 * 2 * 3 * 4 = 24
#Write a program that lets the user enter a nonnegative integer and then uses a loop to calculate
#the factorial of that number. Display the factorial.

number = int(input("enter a number : "))
for i in range (1,number):
    number = i * number
    print(f"{i} : {number}")
