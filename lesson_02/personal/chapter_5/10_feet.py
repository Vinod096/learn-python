#One foot equals 12 inches. Write a function named feet_to_inches that accepts a number
#of feet as an argument and returns the number of inches in that many feet. Use the function
#in a program that prompts the user to enter a number of feet and then displays the number
#of inches in that many feet.


def feet_to_inches():
    feet = int(input("enter number of feets :"))
    inches = feet * 12
    return inches

def main():
    number_of_inches = feet_to_inches()
    print("total number of inches :",number_of_inches)

main()
