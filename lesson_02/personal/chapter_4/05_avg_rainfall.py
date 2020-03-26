#Write a program that uses nested loops to collect data and calculate the average rainfall
#over a period of years. The program should first ask for the number of years. The outer loop
#will iterate once for each year. The inner loop will iterate twelve times, once for each month.
#Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
#After all iterations, the program should display the number of months, the total inches of
#rainfall, and the average rainfall per month for the entire period.

years = 0
months = 0
years = int(input("please enter year : "))
for years in range (1,years + 1):
    for i in range (1,13):
        inches = int(float(input("enter inches of rainfall : ")))
        months = months + inches
        print("rainfall is : ",months)
    print("total rainfall in inches is :",months)
number_of_months = years * 12
average_rainfall = months / number_of_months
print("average rainfall is : ",average_rainfall)



