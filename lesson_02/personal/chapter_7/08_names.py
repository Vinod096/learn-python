#If you have downloaded the source code from this book’s companion Web site, you will find
#the following files in the Chapter 07 folder:
#• GirlNames.txt—This file contains a list of the 200 most popular names given to girls
#born in the United States from the year 2000 through 2009.
#• BoyNames.txt—This file contains a list of the 200 most popular names given to boys
#born in the United States from the year 2000 through 2009.
#Write a program that reads the contents of the two files into two separate lists. The user
#should be able to enter a boy’s name, a girl’s name, or both, and the application will display
#messages indicating whether the names were among the most popular.

b_names = open('boys_names.txt','r')
boys_name = b_names.read()
g_names = open('girls_names.txt','r')
girls_names = g_names.read()
all_names = boys_name + girls_names
boys_name_search = str(input("Enter a boy name : ")).lower()
girls_name_search = str(input("Enter a girl name : ")).lower()
if boys_name_search in boys_name:
    print("You've entered a most popular name among boys name list.")
else:
    print("Entered name is not in most popular boys name list")
if girls_name_search in girls_names:
    print("You've entered a most popular name among girls name list.")
else:
    print("Entered name is not in most popular girls name list")
if boys_name_search in all_names and girls_name_search in all_names:
    print("You've entered a most popular names in boys name list and girls names list.")
else:
    print("The names you've entered is not in neither boys nor in girls names lists")
