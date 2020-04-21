#Assume that a file containing a series of integers is named numbers.txt and exists on the
#computer’s disk. Write a program that reads all of the numbers stored in the file and calculates
#their total.

int_numbers = open('numbers.txt','r')
number_1 = int(int_numbers.readline())
number_2 = int(int_numbers.readline())
number_3 = int(int_numbers.readline())
number_4 = int(int_numbers.readline())
number_5 = int(int_numbers.readline())

total = number_1 + number_2 + number_3 + number_4 + number_5

print("Given numbers are :",number_1,number_2,number_3,number_4,number_5)
print("total of given numbers :",total)
int_numbers.close()