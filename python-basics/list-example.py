# INITIALIZE A SIMPLE LIST OBJECT

user_list = ["ankit","helen","pravin"]

# INDEXING A LIST
# INDEXING ON A LIST HAPPENS ON THE COMMA LEVEL
#print(user_list[0][0])

# CHANGE VALUES IN A LIST - NOT ALLOWED IN A STRING
user_list[1] = "Saketh"
#print(user_list)

# APPEND OBJECT TO A LIST
user_list.append("Sushma")
#print(user_list)

# POP AN OBJECT FROM THE LIST
user_list.pop(0)
#print(user_list)

# NESTED LIST
complex_list = [["ankit","helen"],["pravin","robinson"],["stephen","vijay"]]
print(complex_list[0][1][0])