def pos_neg(value1, value2, both):  
    '''
    To define the function 'pos_neg' with 2 arguments in one parameter
    ''' 
    both = value1 and value2  # if two values are the same
    if value1 <= 0 and value2 >= 0 or value1 >= 0 and value2 <= 0 or both <= 0:
         return True  # if both are negative
     else: 
