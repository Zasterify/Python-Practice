def open_school(covid, school, tuition):   
    """
    To define the function 'open_school' with three 3 arguments 'covid' 'school' and 'tuition' 
    """
    if not covid and school and tuition:  # if covid is false, school is true and tuition is true
        return ('SCHOOL IS OPEN FOR IN PERSON INSTRUCTION')  # To print this statement
    
    elif not covid and school and not tuition:  # if covid is false, school is true and tuition is false
        return ('SCHOOL IS OPEN, BUT YOU HAVE NOT PAID')  # To print this statement

    elif covid or not school and tuition:  # if covid is true, school is false and tuition is true
        return ('SCHOOL IS CLOSED FOR IN PERSON INSTRUCTION. PLEASE STAY HOME FOR ONLINE LEARNING')  # To print this statement
    else:  # if covid is false, school is false and tuition is false
        return ('SEEK FURTHER INSTRUCTION BY CONTACTING THE SCHOOL') # To print this statement

print(open_school(False, False, False))  # To print this to call the function 'open_school'


