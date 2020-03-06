Total_no_of_cookies = 48
cups_of_sugar = 1.5
cups_of_butter = 1
cups_of_flour = 2.75
#**********************************************#

print("Given values are :- ")
print("Total no of cookies =",Total_no_of_cookies)
print("cups of sugar =",cups_of_sugar)
print("cups of butter =",cups_of_butter)
print("cups of flour =",cups_of_flour)

#***********************************************#
No_of_cookies_Req = float(input("cookies required :"))
ReqSugar = (No_of_cookies_Req / Total_no_of_cookies) *  cups_of_sugar
print("No of cups of SugarReq :",ReqSugar)
ReqButter = (No_of_cookies_Req / Total_no_of_cookies) * cups_of_butter
print("No of cups of ButterReq :",ReqButter)
FlourReq = (No_of_cookies_Req / Total_no_of_cookies) * cups_of_flour
print("No of cups of FlourReq :",FlourReq)