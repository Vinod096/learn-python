#There are three seating categories at a stadium. For a softball game, Class A seats cost $20,
#Class B seats cost $15, and Class C seats cost $10. Write a program that asks how many
#tickets for each class of seats were sold, and then displays the amount of income generated
#from ticket sales.

def class_A():
    A_class = int(input("Enter number of seats in A :"))
    A_amount = A_class * 20
    return A_amount

def class_B():
    B_class = int(input("Enter number of seats in B :"))
    B_amount = B_class * 15
    return B_amount

def class_C():
    C_class = int(input("Enter number of seats in C :"))
    C_amount = C_class * 10
    return C_amount

def total(A_amount,B_amount,C_amount):
    total_seats = A_amount +B_amount + C_amount
    return total_seats

def main():
    income_of_A = class_A()
    income_of_B = class_B()
    income_of_C = class_C()
    total_income = total(income_of_A,income_of_B,income_of_C)
    print("amount of income generated from class A :",income_of_A)
    print("amount of income generated from class B :",income_of_B)
    print("amount of income generated from class C :",income_of_C)
    print("total income generated from three classes is :",total_income)

main()
