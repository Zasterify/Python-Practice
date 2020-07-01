meal = float(input("How much was your meal?: "))  # To put the price of meal
tip = int(input("What percentage tip would you like to give?: ")) # To put the percentage whatever you want
final_tip = (float(tip / 100 * meal))  # To calculate the final tip
final_price = (float(final_tip + meal))  # To calculate the final price
print("You will be tipping $",final_tip, " Your final total will be $",final_price, "Have a nice day!")  # To print the whole statement as the above
