#Write a program that uses nested loops to draw this pattern:
##
# #
#  #
#   #
#    #

number = int(input("Enter a number : "))
for r in range (number):
    print("#", end="",sep="")
    for c in range (r):
        print(" ", end="",sep="")
    print("#",sep="")
