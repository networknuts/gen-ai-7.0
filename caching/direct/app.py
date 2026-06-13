import redis
from openai import OpenAI 
from dotenv import load_dotenv
import hashlib 

# SETUP THE ENVIRONMENT
load_dotenv()
client = OpenAI()
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

# HASHING STRATEGY
def convert_key(prompt: str):
    normalized = prompt.strip().lower()
    hashed = hashlib.sha256(normalized.encode()).hexdigest()
    return f"cache:{hashed}"

# LLM RESPONSE
def ask_llm(prompt: str):
    response = client.responses.create(
        model="gpt-5.4-mini",
        input=prompt
    )
    return response.output_text

# MAIN LOGIC

def get_answer(prompt):
    key = convert_key(prompt)
    cached_output = redis_client.get(key)
    if cached_output:
        print("FOUND RESPONSE IN CACHE")
        return cached_output
    else:
        print("INVOKING LLM CALL")
        answer = ask_llm(prompt)
        #IF ANSWER IS FOUND THEN SAVE TO CACHE
        redis_client.set(key,answer)
        return answer 


query = input("Human Query: ")
print("AI RESPONSE\n")
print(get_answer(query))