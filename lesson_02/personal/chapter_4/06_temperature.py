#Write a program that displays a table of the Celsius temperatures 0 through 20 and
#their Fahrenheit equivalents. The formula for converting a temperature from Celsius to
#Fahrenheit is:
#               F= (9/5)C +32
#where F is the Fahrenheit temperature and C is the Celsius temperature. Your program must
#use a loop to display the table.

Fahrenheit = 0
C = 'Celsius'
print("Celsius"  '\t' "Fahrenheit" )
for C in range (0,21):
    Fahrenheit = 9/5 * C + 32
    print(C,'\t',Fahrenheit)
