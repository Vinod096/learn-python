#A retail company must file a monthly sales tax report listing the total sales for the month,
#and the amount of state and county sales tax collected. The state sales tax rate is 5 percent
#and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter the
#total sales for the month. From this figure, the application should calculate and display the
#following:
#• The amount of county sales tax
#• The amount of state sales tax
#• The total sales tax(county plus state)


def state_sales_tax(amount):
    state_tax = 0.05 * amount
    return state_tax

def county_sales_tax(amount):
    county_tax = 0.025 * amount
    return county_tax

def total_Of_taxes(state_tax, county_tax):
    total_taxes = state_tax + county_tax
    return total_taxes

def total_sales(total_taxes,amount):
    total_purchases = total_taxes + amount
    return total_purchases


amount = int(input("Enter total sales :"))

def main():
    s_tax = state_sales_tax(amount)
    c_tax = county_sales_tax(amount)
    t_tax = total_Of_taxes(s_tax, c_tax)
    total = total_sales(t_tax,amount)

    print("state_sales_tax :", s_tax)
    print("county_sales_tax :", c_tax)
    print("total_of_taxes :", t_tax)
    print("total sales(county and sales tax) :", total)

main()
