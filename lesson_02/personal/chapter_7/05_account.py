#If you have downloaded the source code from this book’s companion Web site, you will
#find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
#company’s valid charge account numbers. Each account number is a seven-digit number,
#such as 5658845.
#Write a program that reads the contents of the file into a list. The program should then
#ask the user to enter a charge account number. The program should determine whether
#the number is valid by searching for it in the list. If the number is in the list, the program
#should display a message indicating the number is valid. If the number is not in the list, the
#program should display a message indicating the number is invalid.

acc_numbers = open('charge_accounts.txt','r')
account_numbers = acc_numbers.read()
users_number = str(input("Enter a 7 digits charge account number : "))
if users_number in account_numbers:
    print("Entered number is valid.")
else:
    print("Entered number is invalid")
