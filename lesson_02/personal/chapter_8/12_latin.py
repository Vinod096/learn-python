#Write a program that accepts a sentence as input and converts each word to “Pig Latin.” In
#one version, to convert a word to Pig Latin you remove the first letter and place that letter
#at the end of the word. Then you append the string “ay” to the word. Here is an example:
#English: I SLEPT MOST OF THE NIGHT
#Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY


English = str(input("Enter a sentence : "))
user = English.split(' ')
new_text = []
for letters in user:
    if letters[-1].isalpha():
        new_text.append(letters[1:] + letters[0] + 'ay')
    else:
        new_text.append(letters[1:-1] + letters[0] +'ay' + letters[-1])
pig_latin = ''.join(new_text)
print("pig latin word :",'\n',pig_latin)