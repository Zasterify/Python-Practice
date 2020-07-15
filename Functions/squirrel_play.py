def squirrel_play(temperature, summer):
    '''to define the function called squirrel_play with 2 agruments'''
    if temperature >= 60 and temperature <= 100 and summer:  # if it is summer and temperature is greater than 60 and less than 100
        return True
    elif temperature >= 60 and temperature <= 90 and not summer:  # if it is not summer and temperature is greater than 60 and less than 90
        return True
    else:
        return False

print(squirrel_play(70, False))  # to print for calling the function