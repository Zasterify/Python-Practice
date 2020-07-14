def date_fashion(you, date):  
    '''to define the function called date_fashion with 2 parameter'''
    if you >= 8 or date >= 8:  # if it is greater than 8
        return 2  # to return yes
    elif you <= 2 or date <= 2:  # if it is less than 2
        return 0  # to return no
    else:
        return 1  # to return maybe