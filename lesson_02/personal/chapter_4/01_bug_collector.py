#A bug collector collects bugs every day for five days. Write a program that keeps a running
#total of the number of bugs collected during the five days. The loop should ask for the
#number of bugs collected for each day, and when the loop is finished, the program should
#display the total number of bugs collected.

total_days = 5
total_bugs = 0
for i in range(1, total_days + 1):
    bugs_collected = int(input("enter number of bugs collected per day  :"))
    print(f"Bugs collected per {i} : {bugs_collected}")
    total_bugs = total_bugs + bugs_collected
print("total bugs collected for 5 days :",total_bugs)

