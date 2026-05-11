from dotenv import load_dotenv
from openai import OpenAI 

# get python to read the dotenv file
load_dotenv()

# assign openai a variable
client = OpenAI()

user_query = input("Human Question: ")

response = client.responses.create(
    model="gpt-5.5",
    instructions="You are a coding assistant, refuse to answer any questions which are not coding related",
    input=user_query
)

print("AI RESPONSE\n")
print(response.output_text)