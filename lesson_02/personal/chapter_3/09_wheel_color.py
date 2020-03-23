#On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
#as follows:
#• Pocket 0 is green.
#• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
#pockets are black.
#• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
#pockets are red.
#• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
#pockets are black.
#• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
#pockets are red.
#Write a program that asks the user to enter a pocket number and displays whether the
#pocket is green, red, or black. The program should display an error message if the user
#enters a number that is outside the range of 0 through 36.

number = int(input("enter a number : "))
if number >= 0 and number <= 36:
    print("number is in range")
else:
    print("out of range")
if number == 0:
    print("green")
if number >= 1 and number < 10:
    if number % 2 == 0 :
        print("odd-numbered pockets are red")
    else:
        print("even-numbered pockets are black")
if number >= 11 and number <= 18:
    if number % 2 == 0 :
        print("even-numbered pockets are red")
    else:
       print("odd-numbered pockets are black")
if number >= 19 and number <= 28:
    if number % 2 == 0 :
        print("even-numbered pockets are black.")
    else:
        print("odd-numbered pockets are red")
if number >= 29 and number <= 36:
    if number % 2 == 0:
        print("even-numbered pockets are red")
    else:
        print("odd-numbered pockets are black")
