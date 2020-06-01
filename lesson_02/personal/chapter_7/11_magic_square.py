#The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-8. TheLo Shu Magic Square has the following properties:
#•The grid contains the numbers 1 through 9 exactly.
# • The sum of each row, each column, and each diagonal all add up to the same number.
# This is shown in Figure 7-9.
# In a program you can simulate a magic square using a two-dimensional list. Write a function that accepts a two-dimensional list as an argument and determines whether the list is a Lo Shu Magic Square. Test the function in a program.

import numpy as np

matrix = [[], [], []]

def numbers():
    for num in matrix:
        num = int(input("Enter a number :"))
        matrix[0].append(num)
    for num_1 in matrix:
        num_1 = int(input("Enter a number : "))
        matrix[1].append(num_1)
    for num_2 in matrix:
        num_2 = int(input("Enter a number : "))
        matrix[2].append(num_2)
    return matrix

def number_1(matrix):
    grid = []
    matrix_1 = np.array(matrix[0])
    grid.append(matrix_1)
    return matrix_1

def main():
    values = numbers()
    values_1 = number_1(values)
    print(values)
    print(values_1)

main()