def caught_speeding(speed, birthday):  
    '''to define the function called caught_speeding with 2 arguements'''
    if speed >= 81 and not birthday:  # if it is not birthday and speed is greater than 81
        return 2
    elif speed >= 61 and speed <= 80 and not birthday:  # if it is not birthday and speed is between 61 and 81 
   