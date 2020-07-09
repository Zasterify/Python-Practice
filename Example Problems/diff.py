def diff21(n):  
    '''
    To define the function 'diff21' with one agrument 'n'
    '''
    if n >= 21:  # To notice whether n is greater than 21 or less than 21
        return (n - 21) * 2  # To get the answer which is double if greater than 21
    else:
        return 21 - n  # To get the answer if least than 21

print(diff21(10))  # To print this to call the function 'diff21'


