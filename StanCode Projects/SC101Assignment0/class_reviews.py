"""
File: class_reviews.py
Name: Zining Chen
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


EXIT = -1


def main():
    """
    1. Ask the user to enter which class as course and make the course as upper letter
    2. Check 'course' should enter the loop as it's either SC001 or SC101, or it equals to EXIT.
    3. Define minimum, maximum, count, total for each class
    4. If the course = SC001, the data enter the calculation for SC001.
       If the course = SC101, the data enter the calculation for SC101.
    5. The user can keep entering course and the score until they enter the value for EXIT.
    6. If no score is entered for a certain class, use count = 0 to check.
    """
    course = str(input('Which class?'))
    course = course.upper()
    if course == 'SC001' or 'SC101':
        maximum001 = float('-inf')
        minimum001 = float('inf')
        count001 = 0
        total001 = 0
        maximum101 = float('-inf')
        minimum101 = float('inf')
        count101 = 0
        total101 = 0
        while True:
            data = int(input('Score: '))
            if course == 'SC001':
                if data > maximum001:
                    maximum001 = data
                if data < minimum001:
                    minimum001 = data
                total001 += data
                count001 += 1
            if course == 'SC101':
                if data > maximum101:
                    maximum101 = data
                if data < minimum101:
                    minimum101 = data
                total101 += data
                count101 += 1
            course = str(input('Which class?'))
            course = course.upper()
            if course == str(EXIT):
                if count001 == 0:
                    print('No score for SC001')
                else:
                    average001 = float(total001 / count001)
                    print('=============SC001=============')
                    print('Max (001):  ' + str(maximum001))
                    print('Min (001):  ' + str(minimum001))
                    print('Avg (001):  ' + str(average001))
                if count101 == 0:
                    print('No score for SC101')
                else:
                    average101 = float(total101 / count101)
                    print('=============SC101=============')
                    print('Max (101):  ' + str(maximum101))
                    print('Min (101):  ' + str(minimum101))
                    print('Avg (101):  ' + str(average101))
                break
    elif course == str(EXIT):
        print('No class scores were entered.')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #


if __name__ == '__main__':
    main()
