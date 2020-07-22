def not_string(string):
    '''to define the function called not_string'''
    if string[0:3] == 'not':  # if 'not' aready added to the front of a word
        return string  
    elif string == string:  # if 'not' has added to the front of a word 
        return str('not ') + string  # if 'not' has added to the front of a word

print(not_string('good'))  # to print for calling the function
