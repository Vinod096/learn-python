#Many financial experts advise that property owners should insure their homes or buildings
#for at least 80 percent of the amount it would cost to replace the structure. Write a program
#that asks the user to enter the replacement cost of a building and then displays the
#minimum amount of insurance he or she should buy for the property.

def insurance(value):
    insurance_for_property = (80/100) * value
    return insurance_for_property

def property(value):
    amount = insurance(value)
    print("minimum amount of insurance is :",amount)

value = float(input("enter the value of property: "))

property(value)
