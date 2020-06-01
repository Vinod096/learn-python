#In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list contains numbers. The function should display all of the numbers in the list that are greater than the number n.


def list_of_numbers():
    numbers_list = [1,2,3,4,5,6,7,8,9,10]
    return numbers_list

#def n_number():
#    n = str(input("Enter a n number :"))
#    return n

def compare_list(numbers_list):
    g_numbers = []
    n = int(str(input("Enter a n number :")))
    for n in numbers_list:
        if max(n) in:
            g_numbers.append(numbers_list)
            return g_numbers

def main():
    numbers = list_of_numbers()
#    number_n = n_number()
    compare = compare_list(numbers)
    print("Numbers list :",'\n',numbers)
#    print("Number n :",number_n)
    print("Greater numbers are :",compare)
main()
