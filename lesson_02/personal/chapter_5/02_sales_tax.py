#Write a program that will ask the user to enter the amount of a purchase. The program
#should then compute the state and county sales tax. Assume the state sales tax is 5 percent
#and the county sales tax is 2.5 percent. The program should display the amount of the purchase,
#the state sales tax, the county sales tax, the total sales tax, and the total of the sale
#(which is the sum of the amount of purchase plus the total sales tax).
#Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.

def state_sales_tax(amount):
    state_tax = 0.05 * amount
    return state_tax

def county_sales_tax(amount):
    county_tax = 0.025 * amount
    return county_tax

def total_Of_taxes(state_tax,county_tax):
    total_taxes = state_tax + county_tax
    return total_taxes

def total_of_purchase(amount,total_taxes):
    total_purchases = total_taxes + amount
    return total_purchases

def main(amount):
    s_tax = state_sales_tax(amount)
    c_tax = county_sales_tax(amount)
    t_tax = total_Of_taxes(s_tax,c_tax)
    total = total_of_purchase(amount,t_tax)

    print("state_sales_tax :",s_tax)
    print("county_sales_tax :",c_tax)
    print("total_of_taxes :",t_tax)
    print("total purchase :",total)

amount = int(input("enter the amount of purchases : "))

main(amount)
