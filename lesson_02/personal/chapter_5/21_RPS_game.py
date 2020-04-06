#Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
#The program should work as follows:
#1. When the program begins, a random number in the range of 1 through 3 is generated.
#If the number is 1, then the computer has chosen rock. If the number is 2, then the computer
#has chosen paper. If the number is 3, then the computer has chosen scissors.
# (Don’t display the computer’s choice yet.)
#2. The user enters his or her choice of “rock, ” “paper, ” or “scissors” at the keyboard.
#3. The computer’s choice is displayed.
#4. A winner is selected according to the following rules:
#• If one player chooses rock and the other player chooses scissors, then rock wins.
 #(The rock smashes the scissors.)
#• If one player chooses scissors and the other player chooses paper, then scissors wins.
#(Scissors cuts paper.)
#• If one player chooses paper and the other player chooses rock, then paper wins.
# (Paper wraps rock.)
#• If both players make the same choice, the game must be played again to determine
#the winner.

import random

def ran_numbers():
    number = random.randint(1, 3)
    return number

def computers_choice(number):
    computer_choice = ran_numbers()
    for choice in range (computer_choice) :
        if choice == 1:
            return ("rock")
        if choice == 2:
            return ("Paper")
        if choice == 3:
            return ("Scissors")
    return choice

def players_choice(choice):
    print("choose rock or paper or scissors : ")
    computer = choice
    print("computer choice :",computer)
    while (True):
        player_choice = input("player_choice : ").lower()
        if computer == "rock" and player_choice == "scissors":
            print("rock wins")
            print("The rock smashes the scissors.")
            break
        elif computer == "scissors" and player_choice == "paper":
            print("scissors wins.")
            print("Scissors cuts paper.")
            break
        elif computer == "paper" and player_choice == "rock":
            print("paper wins")
            print("Paper wraps rock.")
            break
        elif computer == player_choice:
            print("play again")
            break
        else:
            print("worng input")
    return computer, player_choice

def main():
    r_numbers = ran_numbers()
    c_choice = computers_choice(r_numbers)
    p_choice = players_choice(c_choice)
    print("random number is :",r_numbers)
    print("computer choice is :",c_choice)
    print("result :",p_choice)

main()
