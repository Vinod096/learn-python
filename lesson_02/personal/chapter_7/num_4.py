#Design a program that asks the user to enter a series of 20 numbers. The program should
#store the numbers in a list and then display the following data:
#• The lowest number in the list
#• The highest number in the list
#• The total of the numbers in the list
#• The average of the numbers in the list

numbers = []

for i in range(1,21):
    num = int(input(f"Enter the number {i}: >>> "))
    numbers.append(num)

lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / 20
print(lowest)
print(highest)
print(total)
print(average)