# This is the answer of number 3 
name1 = int(input("Enter a number: ")) # To assume any number
name2 = int(input("Enter a number: ")) # To put any number
name3 = int(input("Enter a number: ")) # To access any number
if name1 > name2 and name2 > name3:
    print(name1,' is greater and', name3, 'is smaller')
elif name1 > name3 and name3 > name2:
    print(name1, 'is greater and', name2,'is smaller')

elif name2 > name3 and name3 > name1:
     print(name2,' is greater and', name1, 'is smaller')
elif name2 > name1 and name1 > name3:
    print(name2,' is greater and', name3, 'is smaller')

elif name3 > name2 and name2 > name1:
    print(name3,' is greater and', name1, 'is smaller')

elif name3 > name1 and name1 > name2:
     print(name3,' is greater and', name2, 'is smaller')

else:
    print('all the number is the same.')
