def sum_double(value1, value2):  
    '''
    To define the function 'sum_double' with 2 given arguments
    '''
    sum = value1 + value2  # To calculate the sum of value1 and valiue2 
    if value1 == value2:  # if the values are the same or not
        return sum * 2  # To return the answer if they are same
    else:
        return sum  # To return the answer if they are diverse

print(sum_double(1, 2))  # To print this to call the function 'sum_double'
