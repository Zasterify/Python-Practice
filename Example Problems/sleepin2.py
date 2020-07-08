# To define the function 'sleep_in' with two agruments in one parameter 'weekday' and 'vacation'
def sleep_in(weekday, vacation):
    # if you are on vacation especially weekday or not. You have only two options.
    if vacation or not weekday:
        return True  # To return true no matter you can either sleep in or not during vacation
    else:  # If not
        return False  # To return false if you can only sleep in without vacation


print(sleep_in(True, False))  # To print to call the function 'sleep_in'
