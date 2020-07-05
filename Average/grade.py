grade = int(input('Enter your grade: ')) # To ask user for the grade
if grade >= 81:
    print('Your grade is A')  # If it is greater than 80 and return A
elif grade >= 61:
    print('Your grade is B')  # If it is greater than 60 and return B

elif grade >= 51:
    print ('Your grade is C') # If it is greater than 50 and return C
elif grade >= 46:
    print('Your grade is D')  # If it is greater than 45 and return D

elif grade >= 25:
    print('Your grade is E')  # If it is greater than 25 and return E
else:
    print('Your grade is F')  # If it is least than 25 and return F