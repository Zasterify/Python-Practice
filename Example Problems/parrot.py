def parrot_trouble(parrot_talking, hour): 
    '''
    To define the function which is called parrot_trouble with two agruments
    '''
    if parrot_talking and hour <= 7 or parrot_talking and hour >= 20: # Observing whether parrot talking spent either less 7 hours or more than 20 hours
        return True  # To prove how parrot talking spent is true
    else:
        return False  # To get evidence how it is false

print(parrot_trouble(True, 6))  # To print this to call the function