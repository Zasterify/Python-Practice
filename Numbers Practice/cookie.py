num_cookie_jar = int(input("How many cookies do you have in a jar: ")) # To enter the numbers of cookies as you like 
num_people_room = int(input("How many people are in the room?: ")) # To count the number of people in the room 
division = (int(num_cookie_jar // num_people_room)) # To calculate the answer from the above
remainder = (int(num_cookie_jar % num_people_room)) # To count how many cookies are left 
print("Each person can have",division, "cookies, after that, you will have",remainder, "cookie(s) left in the jar.") # To print the full statement

