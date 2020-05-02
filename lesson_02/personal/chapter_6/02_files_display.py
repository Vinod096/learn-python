#Write a program that asks the user for the name of a file. The program should display only
#the first five lines of the file’s contents. If the file contains less than five lines, it should
#display the file’s entire contents.

count = 0
file = str(input("enter file name :"))
print("file name is :",file)
content = open(file,'r')
for i in range (0,5):
    i += count + 1
    print(i)
