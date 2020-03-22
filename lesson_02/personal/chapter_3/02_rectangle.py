#The area of a rectangle is the rectangle’s length times its width. Write a program that asks
#for the length and width of two rectangles. The program should tell the user which rectangle
#has the greater area, or if the areas are the same.

length_of_rectangle_1 = int(input("Enter a number : "))
width_of_rectangle_1 = int(input("Enter a number : "))
area_of_rectangle_1 = length_of_rectangle_1 * width_of_rectangle_1
print("area_of_rectangle_1 :",area_of_rectangle_1)
length_of_rectangle_2 = int(input("Enter a number : "))
width_of_rectangle_2 = int(input("Enter a number : "))
area_of_rectangle_2 = length_of_rectangle_2 * width_of_rectangle_2
print("area_of_rectangle_2 :",area_of_rectangle_2)
if area_of_rectangle_1 == area_of_rectangle_2:
    print("area of two rectangles have same area")
elif area_of_rectangle_1 >= area_of_rectangle_2:
    print("area of rectangel 1 has greater area")
else:
    print("area of rectangle 2 has greater area")

