#Write a program that asks the user to enter five test scores. The program should display a
#letter grade for each score and the average test score. Write the following functions in the
#program:
#• calc_average—This function should accept five test scores as arguments and return
#the average of the scores.
#determine_grade—This function should accept a test score as an argument and return
#a letter grade for the score based on the following grading scale:
#Score Letter Grade
#90–100         A
#80–89          B
#70–79          C
#60–69          D
#Below 60       F

number_of_subjects = 5
max_marks_for_subject = abs(float(input("enter max_marks :")))
total_marks = max_marks_for_subject * 5

def subjects():
    subject_one = abs(float(input("enter the marks for subject_1 : ")))
    if subject_one <= max_marks_for_subject and subject_one != max_marks_for_subject:
        print("in range")
    else:
        print("please enter below max_marks i.e :", max_marks_for_subject)
#----------------------------------------------------#
    subject_two = abs(float(input("enter the marks for subject_2 : ")))
    if subject_two <= max_marks_for_subject and subject_two != max_marks_for_subject:
        print("in range")
    else:
        print("please enter below max_marks i.e :", max_marks_for_subject)
#----------------------------------------------------#
    subject_three = abs(float(input("enter the marks for subject_3 : ")))
    if subject_three <= max_marks_for_subject and subject_three != max_marks_for_subject:
        print("in range")
    else:
        print("please enter below max_marks i.e :", max_marks_for_subject)
#----------------------------------------------------#
    subject_four = abs(float(input("enter the marks for subject_4 : ")))
    if subject_four <= max_marks_for_subject and subject_four != max_marks_for_subject:
        print("in range")
    else:
        print("please enter below max_marks i.e :", max_marks_for_subject)
#----------------------------------------------------#
    subject_five = abs(float(input("enter the marks for subject_5: ")))
    if subject_five <= max_marks_for_subject and subject_five != max_marks_for_subject:
        print("in range")
    else:
        print("please enter below max_marks i.e :", max_marks_for_subject)
    sub_total = subject_one + subject_two + subject_three + subject_four + subject_five
    return sub_total

def average(sub_total, number_of_subjects):
    avg = sub_total / number_of_subjects
    return avg

def percentage_of_marks(sub_total,total_marks):
    percentage = (sub_total / total_marks) * 100
    if percentage < 100 and percentage > 90:
        print("A")
    if percentage < 89 and percentage > 80:
        print("B")
    if percentage < 79 and percentage > 70:
        print("C")
    if percentage < 69 and percentage > 60:
        print("D")
    if percentage < 60 :
        print("F")
    return percentage

def main():
    subjects_total = subjects()
    avg_of_subjects = average(subjects_total,number_of_subjects)
    marks_percentage = percentage_of_marks(subjects_total,total_marks)
    print("total of 5 subjects : ",subjects_total)
    print("average marks :",avg_of_subjects)
    print("percentage :",marks_percentage)

main()
