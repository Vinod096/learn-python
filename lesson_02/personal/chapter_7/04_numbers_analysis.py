#Design a program that asks the user to enter a series of 20 numbers. The program should
#store the numbers in a list and then display the following data:
#• The lowest number in the list
#• The highest number in the list
#• The total of the numbers in the list
#• The average of the numbers in the list

total_numbers = 20
list_of_numbers = [0] * 20
index = 0
total = 0
while index < total_numbers:
    print('number -- ', index + 1, ':', sep='', end='')
    list_of_numbers[index] = int(input())
    index += 1
for Value in list_of_numbers:
    total += Value
print("total of numbers is :", total)
average = total / len(list_of_numbers)
print("average of numbers is :", average)
print("Maximum of list of numbers :", max(list_of_numbers))
print("Minimum list of numbers :", min(list_of_numbers))
