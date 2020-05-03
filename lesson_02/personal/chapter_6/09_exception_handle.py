#Modify the program that you wrote for Exercise 6 so it handles the following exceptions:
#• It should handle any IOError exceptions that are raised when the file is opened and data
#is read from it.
#• It should handle any ValueError exceptions that are raised when the items that are read
#from the file are converted to a number.

golf_records = open("golf.txt", "r")
records = golf_records.read()
print("Player's records are :", "\n", records)
golf_records.close()
