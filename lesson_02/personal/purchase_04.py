#A customer in a store is purchasing five items. Write a program that asks for the price of
#each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent.

item_one = int(input('enter the amount : '))
print("amount : ", item_one)
item_two = int(input('enter the amount : '))
print("amount : ", item_two)
item_three = int(input('enter the amount : '))
print("amount : ", item_three)
item_four = int(input('enter the amount : '))
print("amount : ", item_four)
item_five = int(input('enter the amount : '))
print("amount : ", item_five)
sub_total = item_one + item_two + item_three + item_four + item_five
print("sub_total is : ", sub_total)
sales_tax = (sub_total * 7)/100
print("sales tax is :",sales_tax)
total_sales = sub_total + sales_tax
print("total sales is :",total_sales)
