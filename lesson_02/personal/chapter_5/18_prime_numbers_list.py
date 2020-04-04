#This exercise assumes that you have already written the is_prime function in Programming
#Exercise 17. Write another program that displays all of the prime numbers from 1 to 100.
#The program should have a loop that calls the is_prime function.

def prime_list():
    for number in range (1,101):
        if number > 1:
            for i in range (2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)
    return number

def main():
    prime_numbers = prime_list()
    print(prime_numbers)

main()
