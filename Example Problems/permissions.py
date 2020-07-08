def permission(dad, mom):  
    """
    To define the function 'permission' with 2 arguments 'dad' and 'mom' 
    """
    if dad and mom:  # if mom and dad are permitted Deborah to play soccer 
        return True   # if permission is true, then she is allowed to play it
    else:
        return False  # if permission is false, then she is not allowed to play it

print(permission(True, True))  # To print to call the function 'permission'