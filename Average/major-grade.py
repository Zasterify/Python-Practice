major = input('Enter your major: ')
if major == 'Engineer':
    grade = int(input('Enter your grade: '))
    if grade >= 91:
        print('You have a grade of A in class')
    elif grade >=81:
        print('You have a grade of B in class')
    elif grade >= 71:
        print('You have a grade of C in class')
    elif grade >= 61:
        print('You have a grade of D in class')
    elif grade <= 60:
        print('You have a grade of F in class')

elif major == 'Art':
    grade = int(input('Enter your grade: '))
    if grade >= 81:
        print('You have a grade of A in class')
    elif grade >=61:
        print('You have a grade of B in class')
    elif grade >= 41:
        print('You have a grade of C in class')
    elif grade >= 21:
        print('You have a grade of D in class')
    elif grade <= 20:
        print('You have a grade of F in class')

elif major == 'General':
    grade = int(input('Enter your grade: '))
    if grade >= 41:
        print('You have a grade of A in class')
    elif grade >=31:
        print('You have a grade of B in class')
    elif grade >= 21:
        print('You have a grade of C in class')
    elif grade >= 11:
        print('You have a grade of D in class')
    elif grade <= 10:
        print('You have a grade of F in class')
