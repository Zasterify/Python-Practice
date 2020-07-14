def squirrel_play(temperature, summer):  
    '''to define the function called squirrel_play with 2 agruments'''
    if temperature >= 60 and temperature <= 90 and not summer:  # to check whether temperature is greater than 60 and less than 90 and not summer
        return True
    elif summer and temperature > 70:  # if summer and temperature is greater than 70
        return True
    else:
        return False

