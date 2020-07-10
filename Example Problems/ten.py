def makes10(a, b):  
    '''
    To define the function which is called 'makes10' with 2 arguments 'a' and 'b' 
    '''
    sum = a + b  # To make a total of a and b
    if a == 10 or b == 10 or sum == 10:  # To notice which one of them that can give 10
        return True  # To get the answer whether a or b or sum is right
    else:
        return False  # To get the answer whether a or b or sum is wrong

print(makes10(9, 9))  # To print this to call the function




