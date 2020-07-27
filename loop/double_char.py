def double_char(word):  
    '''to define the function called double_char with a given string'''
    result = ''
    for char in word:  # for each in word
        result += char * 2  # to calculate for the result
    return result  # to return doubled for each of them

print(double_char('The'))  # to print for calling the function