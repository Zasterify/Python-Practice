def sleep_in(weekday, vacation):  # To define the function 'sleep_in' consits with 'weekday' and 'vacation'
    if not weekday:  # If it is not weekday 
        return True  # You can only sleep in
    else:            # if stuck
        return False  # You can't sleep in

    if vacation:  # If it is on vacation
        return True  # You can sleep in
    else:            # if stuck
        return False # You can't sleep in

print(sleep_in(False, True)) # You have to call your function at the end 
# for it to do things. It is like making a calculator. You have made the calculator,
# Now you have to give the calculator things to calculate