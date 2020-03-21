max_marks_for_subject = abs(float(input("enter max_marks :")))
total_marks = max_marks_for_subject * 5

#------------------------------------------------------#

subject_one = abs(float(input("enter the marks for subject_1 : ")))
if subject_one <= max_marks_for_subject and subject_one != max_marks_for_subject:
    print("in range")
else:
    print("please enter below max_marks i.e :",max_marks_for_subject)

#------------------------------------------------------#

subject_two = abs(float(input("enter the marks for subject_2 : ")))
if subject_two <= max_marks_for_subject and subject_two != max_marks_for_subject:
    print("in range")
else:
    print("please enter below max_marks i.e :", max_marks_for_subject)

#------------------------------------------------------#

subject_three = abs(float(input("enter the marks for subject_3 : ")))
if subject_three <= max_marks_for_subject and subject_three != max_marks_for_subject:
    print("in range")
else:
    print("please enter below max_marks i.e :", max_marks_for_subject)

#------------------------------------------------------#

subject_four = abs(float(input("enter the marks for subject_4 : ")))
if subject_four <= max_marks_for_subject and subject_four != max_marks_for_subject:
    print("in range")
else:
    print("please enter below max_marks i.e :", max_marks_for_subject)

#------------------------------------------------------#

subject_five = abs(float(input("enter the marks for subject_5: ")))
if subject_five <= max_marks_for_subject and subject_five != max_marks_for_subject:
    print("in range")
else:
    print("please enter below max_marks i.e :", max_marks_for_subject)

#------------------------------------------------------#

sub_total = subject_one + subject_two + subject_three + subject_four + subject_five
print("total marks are :",sub_total)

#------------------------------------------------------#

percentage = (sub_total / total_marks) * 100
print("percentage is :",percentage)

if percentage <= 100 and percentage >= 75:
    print("outstanding")

if percentage <= 74 and percentage >= 60:
    print("first class")

if percentage <= 59 and percentage >= 35:
    print("second class")

if percentage <= 34 and percentage >= 0:
    print("below second class or failed")
