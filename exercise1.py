
""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion
This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.
Example:
$ python exercise1.py
"""
__author__ = 'Xiuhua Ke'
__email__ = "xiuhua.ke@mail.utoronto.ca"
__copyright__ = "2014 Xiuhua Ke"
# imports one per line

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.
    :param:
    grade (integer or string): Grade to be converted
    If integer, accepted values are 0-100.
    If string, accepted values are A+, A, A-, B+, B, B-, FZ
    :return:
    float: The equivalent GPA
    Value is 0.0-4.0
    :raises:
    TypeError if parameter is not a string or integer
    ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0
    if type(grade) is str:
        # check that the grade is one of the accepted values
        if (grade == "A+") or (grade == "A") or (grade == "A-") or (grade == "B+") or (grade == "B") or (grade == "B-") or (grade == "FZ"):
            # assign grade to letter_grade
            letter_grade = grade
        else:
            print("error")
            raise ValueError("parameter is out of range")

    elif type(grade) is int:
        # check that grade is in the accepted range
        if (grade >=0) and (grade <=100):
            # convert the numeric grade to a letter grade
            if (grade >=0)and (grade <=69):
                letter_grade = "FZ"
            elif (grade >= 70) and (grade <= 72):
                letter_grade = "B-"
            elif (grade >= 73) and (grade <= 76):
                letter_grade = "B"
            elif (grade >= 77) and (grade <= 79):
                letter_grade = "B+"
            elif (grade >= 80) and (grade <= 84):
                letter_grade = "A-"
            elif (grade >= 85) and (grade <= 89):
                letter_grade = "A"
            elif (grade >= 90) and (grade <= 100):
                letter_grade = "A+"
        else:
            print("error")
            raise ValueError("200 is out of the range")
            # assign the value to letter_grade
            # hint: letter_grade = mark_to_letter(grade)
    else:
        # raise a TypeError exception
        print ("error")
        raise TypeError("Invalid type passed as parameter")
        # write a long if-statement to convert letter_grade
        # assign the value to gpa

    # convert the letter grade to gpa
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    else:
        gpa = 0.0


    return gpa

grade_to_gpa("A+")

