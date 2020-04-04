#In this chapter, you saw an example of how to write an algorithm that determines whether
#a number is even or odd. Write a program that generates 100 random numbers and keeps
#a count of how many of those random numbers are even and how many of them are odd.

import random

def ran_numbers():
    number = 0
    for number in range (1, 101):
        number = random.randint(1, 100)
    return number

def odd(number):
    for number in (1, number + 1):
        count = 0
        if number % 2 != 0:
            count = count + 1
    return count

def even(number):
    for number in (1, number + 1):
        count = 0
        if number % 2 == 0:
            count = count + 1
    return count

def main():
    random_numbers = ran_numbers()
    even_numbers = even(random_numbers)
    odd_numbers = odd(random_numbers)
    print("random numbers :",random_numbers)
    print("number of even numbers :",even_numbers)
    print("number of odd numbers :",odd_numbers)

main()
