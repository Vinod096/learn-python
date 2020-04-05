#Write a program that generates a random number in the range of 1 through 100, and
#asks the user to guess what the number is. If the user’s guess is higher than the random
#number, the program should display “Too high, try again.” If the user’s guess is lower than
#the random number, the program should display “Too low, try again.” If the user guesses
#the number, the application should congratulate the user and then generate a new random
#number so the game can start over.
#Optional Enhancement: Enhance the game so it keeps count of the number of guesses that
#the user makes. When the user correctly guesses the random number, the program should
#display the number of guesses.

import random

def ran_numbers():
    number = 0
    value = int(input("enter a value : "))
    for number in range(1, 101):
        number = random.randint(1, 100)
        print(f"{number}")
        if number == value :
            print("random number is equal to given value")
        elif number >= value :
            print("Too high, try again.")
        else:
            print("Too low, try again.")
    return number

def main():
    ran_number = ran_numbers()
    print("random number :",ran_number)

main()