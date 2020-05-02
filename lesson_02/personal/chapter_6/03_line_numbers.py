#Write a program that asks the user for the name of a file. The program should display the
#contents of the file with each line preceded with a line number followed by a colon. The
#line numbering should start at 1.

count = 0
file = str(input("enter file name :"))
print("file name is :", file)
content = open(file, 'r')
for i in range(0, 10):
    i += count + 1
    print(f"{i} :",i)
