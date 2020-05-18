#Write a program that gets a string containing a person’s first, middle, and last names,and then display their first, middle, and last initials. For example, if the user enters John William Smith the program should display J. W. S.


first_name = str(input("Enter First Name : "))
middle_name = str(input("Enter Middle Name : "))
last_name = str(input("Enter Last Name : "))
print("Initials of persons names : ", '\n',first_name[0],'\n', middle_name[0],'\n', last_name[0])

