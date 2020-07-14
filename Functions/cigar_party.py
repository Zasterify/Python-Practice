def cigar_party(num_cigar, weekend):  
    '''to define the function called cigar_party with 2 parameters'''
    if num_cigar >= 40 and num_cigar <=60 and not weekend:  # to notice whether num of cigars is greater than 40 and less than 60 and not weekend
        return True
    elif weekend and num_cigar >= 40:  # if weekend and num_cigar is greater than 60`
        return True
    else:
        return False

print(cigar_party(70, True))  # to print for calling the function 

