def pos_neg(value1, value2, both):  
    '''
    To define the function 'pos_neg' with 2 arguments in one parameter
    ''' 
    both = value1 and value2  # if two values are the same
    if value1 <= 0 and value2 >= 0 or value1 >= 0 and value2 <= 0 or both <= 0:  # to observe as if value1 is either positive or negative and value2 is either negative or positive
        return True  # if both are negative
    else:
        return False  # if both are not negative  

print(pos_neg(-4, -5, True))  # To print to call the function 'pos_neg'