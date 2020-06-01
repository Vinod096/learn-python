#Write a program with a function that accepts a string as an argument and returns the
#number of vowels that the string contains. The application should have another function
#that accepts a string as an argument and returns the number of consonants that the string
#contains. The application should let the user enter a string and should display the number
#of vowels and the number of consonants it contains.

user = str(input("Enter a word or sentense :"))
vowels = 0
consonants = 0
for i in user:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        vowels += 1
    else:
        consonants += 1
print("number of vowels in sentense :",vowels)
print("number of consonants in sentense :",consonants)
