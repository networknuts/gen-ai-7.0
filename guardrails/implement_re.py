import re 

USER_INPUT = """
Hi, my name is aryan. please draft an email from 
aryan@gmail.com to my employer at info@networknuts.net
asking for 7 days of PTO.
"""

normalized_input = USER_INPUT.lower()

sanitized_input = re.sub(r"\w+@\w+\.\w+","<EMAIL_ADDRESS>",normalized_input)

print(sanitized_input)