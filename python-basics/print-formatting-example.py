# THIS IS A COMMENT, IT IS NOT CONSIDERED AS CODE

#asking basic data from the user
user_name = input("what is your user name? ")
user_id = input("what is your ID? ")
user_location = input("what is your location? ")

#printing the information using print formatting f method
print(f"Hello, your name is {user_name}. Your ID is {user_id} and your location is {user_location}.")

#printing using the dot format method
print("Hello, your name is {}. Your ID is {} and your location is {}".format(user_name,user_id,user_location))