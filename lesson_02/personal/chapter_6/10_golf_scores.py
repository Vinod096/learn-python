#The Springfork Amateur Golf Club has a tournament every weekend. The club president has asked you to write two programs:
#1. A program that will read each player’s name and golf score as keyboard input, and thensave these as records in a file named golf.txt. (Each record will have a field for the player’s name and a field for the player’s score.)
#2. A program that reads the records from the golf.txt file and displays them.

while (True):
    golf_club = open("golf.txt", "w")
    player_name = str(input("Enter player name : "))
    score = int(input("Enter score : "))
    golf_club.write(str(player_name) + "\t")
    golf_club.write(str(score))
    print("Do you want to add another player name and score : ")
    choice = input("Enter yes or no : ").lower()
    if choice == 'yes':
        continue
    else:
        break
golf_club.close()
golf_records = open("golf.txt","r")
records = golf_records.readline()
print("Player's records are :","\n",records)
golf_records.close()
