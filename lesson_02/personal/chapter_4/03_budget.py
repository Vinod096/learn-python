#Write a program that asks the user to enter the amount that he or she has budgeted for
#a month. A loop should then prompt the user to enter each of his or her expenses for the
#month and keep a running total. When the loop finishes, the program should display the
#amount that the user is over or under budget.

budget_for_a_month = float(input("enter budget for a month : "))
print(budget_for_a_month)
total = 0
while(True):
    value = float(input("Add expense : "))
    total = total + value
    print("Do you want to add another expense ")
    choice = input("Enter Yes or No : ").lower()
    if (choice == 'yes'):
        continue
    else:
        print(total)
        if (total > budget_for_a_month):
            print("Over Budget")
        else:
            print("Under Budget")
        break