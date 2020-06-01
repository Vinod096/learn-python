#Write a program that accepts as input a sentence in which all of the words are run together
#but the first character of each word is uppercase. Convert the sentence to a string in which
#the words are separated by spaces and only the first word starts with an uppercase letter.
#For example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
#he roses.”

char = str(input("Enter a sentence : "))
char_1 = char.capitalize()
char_1 = char.split()
print("Modified sentence : ",'\n',char_1)
char_1 = '\t'.join(char_1)
print("Words separated by space : ",'\n',char_1)
