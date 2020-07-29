def end_other(str1, str2):
    ''' To define the function 'end_other' with only 2 arguments'''
    if str1[2:] == str2:  # if str1 at index 2 is equal to str2
        return True
    elif str2[2:] == str1: # if str2 at index 2 is equal to str2
        return True
    else:
        return False

print(end_other('Hiabc','abc' ))  # to print for calling the function