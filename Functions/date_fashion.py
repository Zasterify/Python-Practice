def date_fashion(you, date):  
    '''to define the function called date_fashion with 2 parameter'''
    if you <= 2 or date <= 2:  # if it is less than 2
        return 0  # to return no
    elif you >= 8 or date >= 8:  # if it is greater than 8
        return 2  # to return yes
    else:
        return 1  # to return maybe

print(date_fashion(5,10))  # to print for calling the function