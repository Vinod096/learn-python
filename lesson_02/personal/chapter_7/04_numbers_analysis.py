#Design a program that asks the user to enter a series of 20 numbers. The program should
#store the numbers in a list and then display the following data:
#• The lowest number in the list
#• The highest number in the list
#• The total of the numbers in the list
#• The average of the numbers in the list

total_numbers = []
for i in range (1,21):
    numbers = int(str(input(f"Enter number {i} : ")))
    total_numbers.append(numbers)
total = sum(total_numbers)
print("total of numbers is :", total)
average = total / len(total_numbers)
print("average of numbers is :", average)
print("Maximum of list of numbers :", max(total_numbers))
print("Minimum list of numbers :", min(total_numbers))
