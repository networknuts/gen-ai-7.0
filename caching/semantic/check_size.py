from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# EMBEDDING MODEL STRATEGY
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

result = get_embedding("what is the capital of india?")
print(len(result))