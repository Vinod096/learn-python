#Write a function named max that accepts two integer values as arguments and returns the
#value that is the greater of the two. For example, if 7 and 12 are passed as arguments to
#the function, the function should return 12. Use the function in a program that prompts the
#user to enter two integer values. The program should display the value that is the greater
#of the two.

def value_1():
    number_1 = int(input("enter value 1 : "))
    return number_1

def value_2():
    number_2 = int(input("enter value 2 : "))
    return number_2

def max(value_1,value_2):
    if value_1 > value_2 :
        return value_1
    else:
        return value_2

def main():
    number_1 = value_1()
    number_2 = value_2()
    max_value = max(number_1,number_2)
    print("number 1 :",number_1)
    print("number 2 :",number_2)
    print("greater number :",max_value)

main()