#Assume that a file containing a series of names(as strings) is named names.txt and exists
#on the computer’s disk. Write a program that displays the number of names that are stored
#in the file. (Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number of items that are read from the file.)

count = 0
names = open("names.txt","r")
count = names.readlines()
number_of_items = len(count)
print("number of items :",number_of_items)
