#Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the form March 12, 2014.

month = str(input("Enter month : "))
date = str(input("Enter date : "))
year = str(input("Enter year : "))
print("Date :",'\n',month[0:10],date[0:2],',',year [0:4])

