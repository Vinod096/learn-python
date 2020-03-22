#Write a program that asks the user for a number in the range of 1 through 7. The program
#should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
#3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
#display an error message if the user enters a number that is outside the range of 1 through 7.

days_number = int(input("Enter a number : "))
if days_number == 1 :
    print("monday")
elif days_number == 2 :
    print("tuesday")
elif days_number == 3 :
    print("wednesday")
elif days_number == 4 :
    print("thursday")
elif days_number == 5 :
    print("friday")
elif days_number == 6 :
    print("saturday")
elif days_number == 7 :
    print("sunday")
else:
    print("out of days_number")