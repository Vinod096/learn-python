#If you have downloaded the source code from this book’s companion Web site, you will
#find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored
#as one sentence per line. Write a program that reads the file’s contents and calculates the
#average number of words per sentence.

text_file = open('named_text.txt','r')
length = len(text_file.readline())
print("average number of words :",length)
text_file.close()
