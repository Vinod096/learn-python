from secrets import choice
from tkinter.messagebox import YES

from sqlalchemy import true
from sympy import And

def customer():
    user = str(input("What type of food you requried : "))
    if user == 'burgers':
        print("Food item is available")
    else:
        print("You've entered unavailable item ")
        exit()
    return user

def order_burgers(user) :
    food_burgers = []

    burgers = {'McDonalds': 'McSpicy Chicken Burger, 20$','Hungry Jacks': 'Double Tender Crispy Chicken Burger,15$', 'Grilld': 'Chicken Burger, 25$ \n Beef Burger, 15$'}

    while (True):
            restuarant_name = str(input("Enter name of the resturant : "))
            if (restuarant_name == 'McDonalds'):
                print ("Resturant contains following Burgers : \n ",burgers['McDonalds'])
                food_burgers.append(burgers['McDonalds'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Grilld'):
                print("Resturant contains following Burgers : \n", burgers['Grilld'])
                food_burgers.append(burgers['Grilld'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True

            if (restuarant_name == 'Hungry Jacks'):
                print("Resturant contains following Burgers : \n ", burgers['Hungry Jacks'])
                food_burgers.append(burgers['Hungry Jacks'])
                choice = input('Do you want to more food items (Yes / No ) : ')
                if choice == "yes":
                    continue
                elif choice == "no":
                    print("Thanks for Ordering..!")
                    print("Your order has been sent to Restaurant. Enjoy your food")
                    return True
            else:
                print("Please enter valid restaurant name")
                break
    return food_burgers

def main() :
    person = customer()
    burgers_order = order_burgers(person)
main()

