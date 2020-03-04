sales_tax = 0.07
item_one = int(input('enter the amount : '))
print("amount : ",item_one)
item_two = int(input('enter the amount : '))
print("amount : ",item_two)
item_three = int(input('enter the amount : '))
print("amount : ",item_three)
item_four = int(input('enter the amount : '))
print("amount : ",item_four)
item_five = int(input('enter the amount : '))
print("amount : ",item_five)
sub_total = item_one + item_two + item_three + item_four + item_five
print("sub_total is : ",sub_total)
total_sales = sub_total + sales_tax
print("total_sales are : ",total_sales)
