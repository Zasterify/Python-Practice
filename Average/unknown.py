num = int(input('Enter a number: '))

if num % 2 == 0:
    if num >= 0 and num <= 50:
        print('Low Even')
    elif num >= 51 and num <= 99:
        print('High Even')
    else:
        print('Unknown Even')
elif num % 2 == 1:
    if num >= 0 and num <= 50:
        print('Low Odd')
    elif num >= 51 and num <= 99:
        print('High Odd')
    else:
        print('Unknown Odd')
else:
    print('unknown number')




        