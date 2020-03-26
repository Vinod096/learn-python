#Write a program that asks the user to enter the amount that he or she has budgeted for
#a month. A loop should then prompt the user to enter each of his or her expenses for the
#month and keep a running total. When the loop finishes, the program should display the
#amount that the user is over or under budget.

budget_for_a_month = int(input("enter budget for a month : "))
expenses = int(input("please enter expenses for month : "))
total_expenses = 0
for i in range (total_expenses == 0):
    total_expenses += expenses
    print(total_expenses)
    if total_expenses < budget_for_a_month :
        print("expenses are under budget")
    else:
       print("expense are over budget")
