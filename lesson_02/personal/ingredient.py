total_no_of_cookies = 48
cups_of_sugar = 1.5
cups_of_butter = 1
cups_of_flour = 2.75
no_of_cookies_req = round(int(input("cookies required :")))
print("no of cookies required in roundup : {0:2f} ".format(no_of_cookies_req))
req_sugar = (no_of_cookies_req / total_no_of_cookies) *  cups_of_sugar
print("no of cups of sugar_required  : {0:.2f}".format(req_sugar))
req_butter = (no_of_cookies_req / total_no_of_cookies) * cups_of_butter
print("no of cups of butter_required : {0:.2f}".format(req_butter))
flour_req = (no_of_cookies_req / total_no_of_cookies) * cups_of_flour
print("no of cups of flour_required : {0:.2f}".format(flour_req))


#Question :
#A cookie recipe calls for the following ingredients:
#• 1.5 cups of sugar
#• 1 cup of butter
#• 2.75 cups of flour
#The recipe produces 48 cookies with this amount of the ingredients. Write a program that
#asks the user how many cookies he or she wants to make, and then displays the number of
#cups of each ingredient needed for the specified number of cookies.
