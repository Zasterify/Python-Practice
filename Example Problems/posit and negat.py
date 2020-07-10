def pos_neg(value1, value2, negative):
    '''
    To define the function 'pos_neg' with 2 arguments in one parameter
    ''' 
    if value1 >= 0 and value2 <= 0 and negative == False:  # if value1 is positive, value 2 is negative and negative is false
        return True 
    elif value1 <= 0 and value2 >= 0 and negative == False:  # if value1 is negative, value2 is postive and negative is false
        return True
    elif value1 <= 0 and value2 <= 0 and negative == True:  # if both are negative and negative is true 
        return True
    else:
        return False

print(pos_neg(-1, 1, False))  # To print to call the function 'pos_neg'