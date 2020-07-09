def open_school(covid, school, tuition):   
    """
    To define the function 'open_school' with three 3 arguments 'covid' 'school' and 'tuition' 
    """
    if not covid and school and tuition:  # if covid is false, school is true and tuition is true
        return ('SCHOOL IS OPEN FOR IN PERSON INSTRUCTION')  # To print this statement
    
    if not covid and school and not tuition:  # if covid is false, school is true and tuition is false


