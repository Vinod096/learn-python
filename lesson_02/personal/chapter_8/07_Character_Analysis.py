#If you have downloaded the source code from this book’s companion Web site, you will
#find a file named text.txt in the Chapter 08 folder. Write a program that reads the file’s
#contents and determines the following:
#• The number of uppercase letters in the file
#• The number of lowercase letters in the file
#• The number of digits in the file
#• The number of whitespace characters in the file

file = open('text.txt','r')
file_1 = file.readline()
print(file_1)
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for i in file_1:
    if (i.isupper()):
        count_1 += 1
    elif (i.islower()):
        count_2 += 1
    elif (i.isnumeric()):
        count_3 += 1
    elif (i.isspace()):
        count_4 += 1
print("Number of uppercase :",count_1)
print("Number of lower case letters :",count_2)
print("Number of digits :",count_3)
print("Number of whitespace characters :",count_4)
file.close()