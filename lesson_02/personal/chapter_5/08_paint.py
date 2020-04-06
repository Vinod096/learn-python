#A painting company has determined that for every 112 square feet of wall space, one gallon
#of paint and eight hours of labor will be required. The company charges $35.00 per
#hour for labor. Write a program that asks the user to enter the square feet of wall space to
#be painted and the price of the paint per gallon. The program should display the following
#data:
#• The number of gallons of paint required
#• The hours of labor required
#• The cost of the paint
#• The labor charges
#• The total cost of the paint job


def paint(wall_space):
    paint_required = (wall_space / 112) * 1
    return paint_required()

def hours_for_labor(wall_space):
    labor_required = (wall_space / 112) * 8
    return labor_required

def paint_cost(paint_required,cost_of_paint):
    price_of_paint = paint_required * cost_of_paint
    return price_of_paint

def charges(labor_required):
    labor_charges = 35 * labor_required
    return labor_charges

def paint_job_cost(price_of_paint,labor_charges):
    total_cost = price_of_paint + labor_charges
    return total_cost

def main():
    gallons_of_paint = paint(wall_space)
    required_labor = hours_for_labor(wall_space)
    cost_paint = paint_cost(gallons_of_paint,cost_of_paint)
    charges_for_labor = charges(required_labor)
    total_price = paint_job_cost(cost_paint,charges_for_labor)
    print("number of gallons of paint required :",gallons_of_paint)
    print("hours of labor required :",required_labor)
    print("cost of the paint :",cost_paint)
    print("labor charges :",charges_for_labor)
    print("total cost of the paint job :",total_price)

wall_space = float(input("Enter wall space : "))
cost_of_paint = int(input("Enter cost of paint : "))

main()

