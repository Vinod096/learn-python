#Assume that a file containing a series of integers is named numbers.txt and exists on the
#computer’s disk. Write a program that displays all of the numbers in the file.

numbers = open('numbers.txt', 'r')
int_numbers = numbers.read()
print(int_numbers)
numbers.close()

