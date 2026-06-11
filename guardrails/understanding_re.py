import re 

f = open("email_list.txt","r")
email_data = f.read()
f.close()

# CHECK IF BOBBY, BOBBI, ROBBY, ROBBI EXISTS
result = re.search(r"[b,r]obb[y,i]",email_data)

# CHECK IF CHR _ _ EXISTS
result = re.search(r"chr[a-z][a-z]",email_data)
result = re.search(r"chr[a-z]{2}",email_data)

# CHECK IF J _ _ _ EXISTS
result = re.findall(r"j[a-z]{3}",email_data)


# CHECK FIRST VALUE STARTING WITH [a-z]
result = re.search(r"[a-z]+",email_data)
result = re.search(r"art[a-z]+",email_data)

# SEARCH FOR AN EMAIL ADDRESS
result = re.search(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9]+",email_data)
result = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9]+",email_data)
result = re.findall(r"\w+@\w+\.\w+",email_data)