#A prime number is a number that is only evenly divisible by itself and 1. For example, the
#number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however,
#is not prime because it can be divided evenly by 1, 2, 3, and 6.
#Write a Boolean function named is_prime which takes an integer as an argument and
#returns true if the argument is a prime number, or false otherwise. Use the function in a
#program that prompts the user to enter a number and then displays a message indicating
#whether the number is prime.

def is_prime():
    number = int(input("enter a number : "))
    if number % 2 != 0 :
        print(f"True,{number} is  a prime number")
        return True
    else:
        print(f"False,{number} is not a prime number")
        return False
    return number

is_prime()
