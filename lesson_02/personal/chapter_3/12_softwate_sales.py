#A software company sells a package that retails for $99. Quantity discounts are given
#according to the following table:
#Quantity Discount
#10–19            10%
#20–49            20%
#50–99            30%
#100 or more      40%
#Write a program that asks the user to enter the number of packages purchased. The program
#should then display the amount of the discount(if any) and the total amount of the
#purchase after the discount.

original_price = 99
Quantity = int(input("enter a number : "))
total_value_of_products = Quantity * original_price
print("total_value_is :",total_value_of_products)
if  Quantity >= 10 and Quantity <= 19 :
    Discount = total_value_of_products * 10 / 100
    print("discount is :",Discount)
if Quantity >= 20 and Quantity <= 49:
    Discount = total_value_of_products * 20 / 100
    print("discount is :",Discount)
if Quantity >= 50 and Quantity <= 99:
    Discount = total_value_of_products * 30 / 100
    print("discount is :", Discount)
if Quantity >= 100:
    Discount = total_value_of_products * 40 / 100
    print("discount is :", Discount)
else:
    print("quatity is less 10 products not eligible for discount")
