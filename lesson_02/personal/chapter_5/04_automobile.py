#Write a program that asks the user to enter the monthly costs for the following expenses
#incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
#maintenance. The program should then display the total monthly cost of these expenses,
#and the total annual cost of these expenses.


def monthly_costs():
    total_expenses = 0
    loan_payment = float(input("enter loan payment :"))
    insurance = float(input("enter insurance amount :"))
    gas = float(input("enter amount for gas :"))
    oil = float(input("enter amount for oil :"))
    tires = float(input("enter amount for tires :"))
    maintenance = float(input("enter amount for maintenance :"))
    total_expenses = total_expenses + loan_payment + insurance + gas + oil + tires + maintenance
    return total_expenses

def total_monthly_costs(total_expenses):
    total = 0
    total = total + total_expenses
    return total

def year_costs(total):
    yearly_expenses = total * 12
    return yearly_expenses

def overall_expenses():
    total_expenses = monthly_costs()
    expenses_per_month = total_monthly_costs(total_expenses)
    expenses_per_year = year_costs(expenses_per_month)
    print("expenses per month are :",expenses_per_month)
    print("expenses per year :",expenses_per_year)

overall_expenses()
