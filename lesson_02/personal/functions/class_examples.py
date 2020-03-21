# DRY - Do not Repeat yourself

# num_one = int(input("Number One >>> "))
# num_two = int(input("Number Two >>> "))

# sum = num_one + num_two


def sum_of_numbers(num_one, num_two):
    return num_one + num_two


result = sum_of_numbers(20, 30)

print(result)

"""
100000 lines
"""

# num_one = int(input("Number One >>> "))
# num_two = int(input("Number Two >>> "))

# sum = num_one + num_two

# print(sum)

# 10000

# print(sum)


def put_pan():
    """
    go to shelf
    take a pan
    clean it
    rub with dry cloth
    put on stove
    """

# with


"""
put pan()
heat pan()
put oil()
make mixture()
put mixture()
keep for 1 min()
flip it()
keep for 1 min()
take out and serve()
"""

# with out

"""
put pan()
heat pan()
put oil
make mixture
put mixture
keep for 1 min
flip it
keep for 1 min
take out and serve
"""

"""
No Return = 1% - Mostly for testing and education
With Return 99% - In Realtime
"""

# Defining a function


def sum_one():
    num_one = int(input("NUM ONE: "))
    num_two = int(input("NUM TWO: "))
    sum = num_one + num_two
    print(sum)

# Calling a function or executing a function


sum_one()


def sum_two():
    num_one = int(input("NUM ONE: "))
    num_two = int(input("NUM TWO: "))
    sum = num_one + num_two
    return sum


result = sum_two()
print(result)
result2 = result + 100
print(result2)

# mode=display ::: https: // cscircles.cemc.uwaterloo.ca/visualize


def add(num_1, num_2):
    return (num_1 + num_2)


def sub(num_1, num_2):
    return (num_1 - num_2)


def calci(add1, sub1):
    return add1 * sub1


def display(cal):
    res = cal(add(1, 2), sub(3, 4))
    print(res)


display(calci)
