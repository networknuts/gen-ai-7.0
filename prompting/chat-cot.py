from dotenv import load_dotenv
from openai import OpenAI 

# get python to read the dotenv file
load_dotenv()

f = open("chain-of-thought.txt","r")
SYSTEM_PROMPT = f.read()
f.close()

# assign openai a variable
client = OpenAI()

user_query = input("Human Question: ")

response = client.responses.create(
    model="gpt-5.5",
    instructions=SYSTEM_PROMPT,
    input=user_query
)

print("AI RESPONSE\n")
print(response.output_text)