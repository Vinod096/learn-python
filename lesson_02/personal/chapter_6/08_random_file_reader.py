#This exercise assumes you have completed Programming Exercise 7, Random Number File
#Writer. Write another program that reads the random numbers from the file, display the
#numbers, and then display the following data:
#• The total of the numbers
#• The number of random numbers read from the file

count = 0
files = open("random_number.txt", "r")
def ran_numbers_in_file():
    count = files.readlines()
    number_of_items = len(count)
    return number_of_items

num = files.readlines()
def sum_of_numbers():
    total = 0
    for total in num:
        total += str(num)
    return total

def main():
    count_of_ran_numbers = ran_numbers_in_file()
    Numbers_total = sum_of_numbers()
    print("Number of random numbers :",count_of_ran_numbers)
    print("Total of random numbers :",Numbers_total)

main()
