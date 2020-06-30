meal = float(input("How much was your meal?: "))  # To put the price of meal
tip = int(input("What percentage tip would you like to give?: ")) # To put the percentage whatever you want
final_tip = (float(tip / 100 * meal))  # To calculate the final tip
final_price = (float( tip + final_tip + meal - tip))  # To calculate the final price
