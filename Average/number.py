num = int(input('Enter a number: ')) # To ask user for any number
if num % 5 == 0 and num % 3 == 0:
    print('FizzBiss')  # If it is divided by both and return FizzBiss
elif num % 5 == 0:
    print('Fizz')  # If it is divided by 5 and return Fizz

elif num % 3 == 0:
    print('Biss')  # If it is divided by 3 and return Biss
else:
    print('The number is',num)  # If it is divided by none of the above and print like this