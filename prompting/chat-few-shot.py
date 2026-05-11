from dotenv import load_dotenv
from openai import OpenAI 

# get python to read the dotenv file
load_dotenv()

# assign openai a variable
client = OpenAI()

# reading the system prompt from an external file
f = open("few-shot-prompts.txt","r")
SYSTEM_PROMPT = f.read()
f.close()

user_query = input("Human Question: ")

response = client.responses.create(
    model="gpt-5.5",
    instructions=SYSTEM_PROMPT,
    input=user_query
)

print("AI RESPONSE\n")
print(response.output_text)