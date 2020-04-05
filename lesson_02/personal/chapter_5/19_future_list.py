#Suppose you have a certain amount of money in a savings account that earns compound
#monthly interest, and you want to calculate the amount that you will have after a specific
#number of months. The formula is as follows:
#F = P * (1 + i)t
#The terms in the formula are:
#• F is the future value of the account after the specified time period.
#• P is the present value of the account.
#• i is the monthly interest rate.
#• t is the number of months.
#Write a program that prompts the user to enter the account’s present value, monthly interest
#rate, and the number of months that the money will be left in the account. The program
#should pass these values to a function that returns the future value of the account, after the
#specified number of months. The program should display the account’s future value.

def time_period():
    future_value = 0
    present_value = int(input("Enter present value : "))
    interest = int(input("Enter a interest : "))
    time = int(input("Enter number of months : "))
    future_value = present_value * (1 + interest) ** time
    return future_value

def main():
    f_value = time_period()
    print("Future value is :",f_value)

main()