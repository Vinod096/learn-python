#Serendipity Booksellers has a book club that awards points to its customers based on the
#number of books purchased each month. The points are awarded as follows:
#• If a customer purchases 0 books, he or she earns 0 points.
#• If a customer purchases 2 books, he or she earns 5 points.
#• If a customer purchases 4 books, he or she earns 15 points.
#• If a customer purchases 6 books, he or she earns 30 points.
#• If a customer purchases 8 or more books, he or she earns 60 points.
#Write a program that asks the user to enter the number of books that he or she has purchased
#this month and displays the number of points awarded.


number_of_books_purchased = int(input("enter the number of books purchased :"))
if number_of_books_purchased == 0 :
    print("you've earned 0 points")
elif number_of_books_purchased < 2 :
    print("earned 0 points")
elif number_of_books_purchased < 4 :
    print("earned 5 points")
elif number_of_books_purchased < 6 :
    print("earned 15 points")
elif number_of_books_purchased < 8 :
    print("earned 30 point")
else:
    print("Congrats, you've earned 60 points")


