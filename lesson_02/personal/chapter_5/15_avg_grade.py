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


def subjects():
    print("Enter 5 subjets :")
    for i in range (1,6):
        number_of_subjects = int(input(f"enter {i} subject : "))
        sub_total = sub_total + number_of_subjects
    return sub_total

def average(sub_total, number_of_subjects):
    avg = sub_total / number_of_subjects
    return avg

def percent(sub_total, number_of_subjects):
    total_marks = 0
    maximum_marks_for_subject = 0
    maximum_marks_for_subject = int(input("Enter maximum marks for subject : "))
    total_marks = maximum_marks_for_subject * number_of_subjects
    percentage = (sub_total / total_marks) * 100
    if percentage <= 100 and percentage >= 90:
        print("A")
    if percentage <= 89 and percentage >= 80:
        print("B")
    if percentage <= 79 and percentage >= 70:
       print("C")
    if percentage <= 69 and percentage >= 60:
        print("D")
    if percentage < 60 and percentage >= 0:
        print("F")
    return percentage

def main():
    total_of_subjects = subjects()
    avg_of_subjects = average(total_of_subjects)
    percentage_of_marks = percent(total_of_subjects)
    print("total of subjects :",total_of_subjects)
    print("avgerage of subjects :",avg_of_subjects)
    print("percentage and grades :",percentage_of_marks)

main()

