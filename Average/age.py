# This is the answer of number 3 
name1 = int(input("Enter a number: ")) # To assume any number
name2 = int(input("Enter a number: ")) # To put any number
name3 = int(input("Enter a number: ")) # To access any number
if name3 < name2 and name2 < name1:
    print(name1 + ' is bigger')
elif name3 < name1 and name1 < name2:
    print(name2,'is bigger')
elif name3 > name2 and name1 < name3:
    print(name3,'is bigger')