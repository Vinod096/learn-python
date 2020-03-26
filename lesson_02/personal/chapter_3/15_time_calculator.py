#Write a program that asks the user to enter a number of seconds and works as follows:
#• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
#than or equal to 60, the program should display the number of minutes in that many
#seconds.
#• There are 3, 600 seconds in an hour. If the number of seconds entered by the user is
#greater than or equal to 3, 600, the program should display the number of hours in that
#many seconds.
#• There are 86, 400 seconds in a day. If the number of seconds entered by the user is
#greater than or equal to 86, 400, the program should display the number of days in that
#many seconds.

seconds = int(input("Please enter number of seconds : "))
if seconds >= 60 :
    minutes = seconds / 60
    print("minutes are :", minutes)
else:
    print("seconds are less the 60")
if seconds >= 3600 :
    hours = seconds / 3600
    print("hours are :",hours)
if seconds >= 86400 :
    days = seconds / 86400
    print("days are :", days)
