user = int(input("Guess a number: ")) # To assume any number
similar = user  # To hold the variable as the above
if user % 2 != 1: #  To put odd number which is exactly correct
    print("The number is wrong!") # If it returns even number and get wrong answer
else:
    print("The number is right!")  # If it returns odd number and get right answer


