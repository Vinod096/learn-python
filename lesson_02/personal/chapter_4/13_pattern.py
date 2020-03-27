#Write a program that uses nested loops to draw this pattern:
#*******
#******
#*****
#****
#***
#**
#*

number = int(input("Enter a number : "))
for r in range(number,0,-1):
    for c in range(1,r + 1):
        print('*', end='')
    print(  )
