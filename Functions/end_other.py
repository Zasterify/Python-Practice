def end_other(str1, str2):
    ''' To define the function 'end_other' with only 2 arguments'''     
    l = str1.upper()    
    i = str2.upper()   
      
    if len(i) == len(i):  # if str1 at index 2 is equal to str2  
        return True    
    elif len(i) == len(l):  # if str2 at index 2 is equal to str2  
        return True  
    elif len(l) == len(i):  
        return True  
    else:  
        return False 

print(end_other('abc', 'abXabc'))  # to print for calling the function