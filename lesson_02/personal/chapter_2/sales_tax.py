#calculation of sales tax
amount_of_purchase = int(input("enter the amount of purchases : "))
print("amount of purchase is : ",amount_of_purchase)
state_sales_tax = 0.05
print("state sales tax is : ", state_sales_tax)
county_sales_tax = 0.025
print("county sales tax is : ", county_sales_tax)
state_sales_tax = state_sales_tax * amount_of_purchase
print("state sales tax is : ",state_sales_tax)
county_sales_tax = county_sales_tax * amount_of_purchase
total_of_purchase = amount_of_purchase + state_sales_tax + county_sales_tax
print("total amount of purchase is : ",total_of_purchase)