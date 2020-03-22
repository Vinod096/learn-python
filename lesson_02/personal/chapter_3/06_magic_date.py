#The date June 10, 1960, is special because when it is written in the following format, the
#month times the day equals the year:
#6/10/60
#Design a program that asks the user to enter a month(in numeric form), a day, and a twodigit
#year. The program should then determine whether the month times the day equals the
#year. If so, it should display a message saying the date is magic. Otherwise, it should display
#a message saying the date is not magic.

date = int(input("enter a number :"))
month = int(input("enter a number :"))
year = int(input("enter a last two digits of year :"))
if year == date * month:
    print("it's magic year")
else:
    print("not a magic year")
