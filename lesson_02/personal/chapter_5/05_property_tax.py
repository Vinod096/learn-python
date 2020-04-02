#A county collects property taxes on the assessment value of property, which is 60 percent
#of the property’s actual value. For example, if an acre of land is valued at $10,000, its
#assessment value is $6, 000. The property tax is then 72¢ for each $100 of the assessment
#value. The tax for the acre assessed at $6, 000 will be $43.20. Write a program that asks for
#the actual value of a piece of property and displays the assessment value and property tax.



def assessment_value(actual_value):
    assess_value = (60/100) * actual_value
    return assess_value

def property_tax(assess_value):
    tax = assess_value * 0.0072
    return tax

def main():
    value = actual_value
    a_value = assessment_value(value)
    p_tax = property_tax(a_value)
    print("Actual value is :",a_value)
    print("Property tax is : {0:.2f}".format(p_tax))

actual_value = float(input("Enter actual value :"))

main()