#Write a program that gives simple math quizzes. The program should display two random
#numbers that are to be added, such as:
#247
#+ 129
#The program should allow the student to enter the answer. If the answer is correct, a message
#of congratulations should be displayed. If the answer is incorrect, a message showing
#the correct answer should be displayed.

def addition():
    sum_of_numbers = int(input("Enter a number : "))
    value_1 = int(input("Enter number 1 : "))
    value_2 = int(input("Enter number 2 : "))
    add = value_1 + value_2
    if sum_of_numbers == add:
        print("Congratulations")
    else:
        return("total of 2 numbers is :",add)
    return add

def main():
    sum = addition()
    print("entered numbers are equal to 2 random numbers i.e :",sum)

main()