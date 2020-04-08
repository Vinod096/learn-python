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

from random import randint

def computers_choice(number):
    if number == 1:
        return ("rock")
    elif number == 2:
        return ("paper")
    else:
        return ("scissors")

def players_choice(computer_choice):
    print("Choose rock or paper or scissors : ")
    computer = computer_choice(randint(1, 3))
    print("computer choice :",computer)
    while (computer):
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
            print("wrong input")
    print(f"Computer: {computer}, Player Choice: {player_choice}")

players_choice(computers_choice)