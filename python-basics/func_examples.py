def say_hello():
    print("hello world")
    print("hello python")
    print("hello AI")

def say_goodbye():
    print("this is the end")
    print("goodbye")

def greetings(username):
    print(f"Hello! {username}, how are you?")

def complex_greeting(username,userlocation):
    print(f"Hello {username}, your location is {userlocation}.")

def add_together(n1=0,n2=0):
    result = n1+n2
    return(result)

def user_data(user_name,user_id):
    return {
        "name": user_name,
        "ID": user_id
    }

def combine_together(n1,n2):
    return [n1,n2]

result = user_data("Ankit","100")
print(result)