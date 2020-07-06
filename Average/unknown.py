num = int(input('Enter a number: '))

if num % 2 == 0:
    if num <= 50:
        print('Low Even')
    if num >= 51 and num <= 99:
        print('High Even')
    else:
        print('Unknown Even')

if num % 2 == 1:
    if num <= 50:
        print('Low Odd')
    if num >= 51 and num <= 99:
        print('High Odd')
    else:
        print('Unknown Odd')
else:
    print('unknown number')




        