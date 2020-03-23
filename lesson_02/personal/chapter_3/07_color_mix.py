#The colors red, blue, and yellow are known as the primary colors because they cannot
#be made by mixing other colors. When you mix two primary colors, you get a secondary
#color, as shown here:
#When you mix red and blue, you get purple.
#When you mix red and yellow, you get orange.
#When you mix blue and yellow, you get green.
#Design a program that prompts the user to enter the names of two primary colors to mix. If
#the user enters anything other than “red, ” “blue, ” or “yellow, ” the program should display
#an error message. Otherwise, the program should display the name of the secondary color
#that results.

primary_colors = print('red','blue','yellow')
color_1 = str(input("enter a color from above list :"))
color_2 = str(input("enter a color from above list :"))
if color_1 == 'red' and color_2 == 'blue' or color_1 == 'blue' and color_2 == 'red':
    print("Secondary color is : Purple")
elif color_1 == 'red' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'red':
    print("Secondary color is : Orange")
elif color_1 == 'blue' and color_2 == 'yellow' or color_1 == 'yellow' and color_2 == 'blue':
    print("Secondary color is : Green")
else:
    print("*please enter a color from given list*")
