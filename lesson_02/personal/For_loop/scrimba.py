names = ['Jane','John','Alena']
names_1 = ['John','Jane','Adeev']
text = 'Welcome to the party'
names.extend(names_1)
for name in range(3):
    names.append(input("enter name :"))
for name in names:
    print(name,text)