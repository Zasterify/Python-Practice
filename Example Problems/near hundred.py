def near_hundred(n): 
    '''
    To define the function 'near_hundred' with one argument 'n'
    '''
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:  # to discover the answer whether n is less than 10 or more than 10
         return True  # if the answer is almost 10