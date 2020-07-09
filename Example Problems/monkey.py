def monkey_trouble(a_smile, b_smile): 
    """
    To define the function 'monkey_trouble' with 2 agruments 'a_smile' and 'b_smile' 
    """
    if a_smile and b_smile or not a_smile and not b_smile:  # if both are smiling or not
         return True  # if a and b are both smiling
    else:
        return False  # if neither a or b is smiling

print(monkey_trouble(False, False))  # To print this to call the function 'monkey_smile'
