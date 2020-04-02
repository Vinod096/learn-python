#A nutritionist who works for a fitness club helps members by evaluating their diets. As part
#of her evaluation, she asks members for the number of fat grams and carbohydrate grams
#that they consumed in a day. Then, she calculates the number of calories that result from
#the fat, using the following formula:
#calories from fat = fat grams * 9
#Next, she calculates the number of calories that result from the carbohydrates, using the
#following formula:
#calories from carbs= carb grams * 4
#The nutritionist asks you to write a program that will make these calculations.

def fat():
    fat_grams = float(input("Enter fat grams :"))
    calories_from_fat = fat_grams * 9
    return calories_from_fat

def carbohydrates():
    carb_grams = float(input("Enter Carbohydrates :"))
    calories_from_carbs = carb_grams * 4
    return calories_from_carbs

def calculations():
    C_fat = fat()
    C_carbohydrates = carbohydrates()
    print("Calories from fat is :{0:.2f}".format(C_fat))
    print("calories from carbohydrates :{0:.2f}".format(C_carbohydrates))

calculations()
