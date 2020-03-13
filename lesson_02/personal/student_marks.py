subject_one = float(input('enter the marks : '))
print("marks : ",subject_one)
subject_two = float(input('enter the marks : '))
print("marks : ", subject_two)
subject_three = float(input('enter the marks : '))
print("marks : ", subject_three)
subject_four = float(input('enter the marks : '))
print("marks : ", subject_four)
subject_five = float(input('enter the marks : '))
print("marks : ", subject_five)
total = subject_one + subject_two + subject_three + subject_four + subject_five
print("total marks are :",total)
average = total /  5
print("average of marks :",average)
if average <= 100 and average >= 75:
    print("outstanding")

if average <= 74 and average >= 60:
    print("first class")

if average <= 59 and average >= 35:
    print("second class")

if average <= 34 and average>= 0:
    print("below second class or failed")
