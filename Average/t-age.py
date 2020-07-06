age = int(input('Enter your age: ')) # To put your age
if age < 18:
    print('You are a minor')
    print('You cannot work legally!')  # If your age is younger than 18 and return like this
else:
    if age >= 18 and age <= 50: 
        print('You are an adult')
        print('You can work legally')   # If your age is older than 18 and return like this
    else: