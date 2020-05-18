#Write a program that writes a series of random numbers to a file. Each random number
#should be in the range of 1 through 500. The application should let the user specify how
#many random numbers the file will hold.

import random

user = int(input("How many random numbers in the file : "))
file = open("random_number.txt","w")
for i in range (1, user + 1):
    ran_numbers = random.randint(1,500)
    file.write(str(ran_numbers)+'\n')
    # print("Random numbers :",ran_numbers)
