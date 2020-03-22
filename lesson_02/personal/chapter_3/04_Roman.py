#Write a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number. If the number is
#outside the range of 1 through 10, the program should display an error message. The following
#table shows the Roman numerals for the numbers 1 through 10:
#Number Roman Numeral
#1          I
#2          II
#3          III
#4          IV
#5          V
#6          VI
#7          VII
#8          VIII
#9          IX
#10         X

number = int(input("enter a number :"))
if number == 1:
    print("Roman number of 1 : I")
elif number == 2:
    print("Roman number of 2 : II")
elif number == 3:
    print("Roman number of 3: III")
elif number == 4:
    print("Roman number of 4 : IV")
elif number == 5:
    print("Roman number of 5 : V")
elif number == 6:
    print("Roman number of 6 : VI")
elif number == 7:
    print("Roman number of 7 : VII")
elif number == 8:
    print("Roman number of 8 : VIII")
elif number == 9:
    print("Roman number of 9 : IX")
elif number == 10:
    print("Roman number of 10 : X")
else:
    print("please enter below 10 or greater the 1")