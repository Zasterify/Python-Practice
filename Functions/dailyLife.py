def shopping(price):  
    '''to define the function called 'shopping' with 1 parameter'''
    return price * 2

def rent(price): 
    '''to define the function called 'rent' with 1 parameter'''
    return price + price * 25/100  # to calculate for increase

def uber(price): 
    '''to define the function called 'uber' with 1 parameter'''
    return price - price * 50/100   # to calculate for discount

def total(shop_price, rent_price, uber_price):
    '''to define the function called 'total' with 3 parameters'''
    print(shopping(shop_price) + rent(rent_price) + uber(uber_price))  # to calculate the amount of prices 

total(1,2,3)
