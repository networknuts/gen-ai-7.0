from openai import OpenAI 
from dotenv import load_dotenv
import requests
import json 
import os 

# SETUP THE ENVIRONMENT
load_dotenv()
client = OpenAI()

f = open("weather_tool_description.txt","r")
function_description = f.read()
f.close()

# CREATE FIRST TOOL - WEATHER DATA
def get_weather(zipcode):
    apikey = os.getenv("WEATHER_API_KEY")
    countrycode = "in"
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"
    result = requests.get(url)
    response = result.json()
    return response 

# CREATE SECOND TOOL - GET ORDER STATUS
def get_delivery_data(user_id):
    url = f"http://localhost:8000/delivery/{user_id}"
    result = requests.get(url)
    if result.status_code != 200:
        return {"Error": "User not found"}
    else:
        return result.json()

# TOOL SCHEMA
openai_tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": function_description,
        "parameters": {
            "type": "object",
            "properties": {
                "zipcode": {
                    "type": "string",
                    "description": "the zipcode of the location to get the weather information of."
                },
            },
            "required": ["zipcode"],
        }
    },
    {
        "type": "function",
        "name": "get_delivery_data",
        "description": "Get delivery details for a user including item, delivery date and status.",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "description": "The ID of the user (1,2,3)"
                }
            },
            "required": ["user_id"],
        }
    }
]

# ASK FOR USER QUERY
user_query = input("HUMAN QUERY: ")

# FIRST LLM CALL 
response = client.responses.create(
    model="gpt-5.4-mini",
    input=user_query,
    tools=openai_tools
)

function_output = []

for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        if item.name == "get_weather":
            result = get_weather(args['zipcode'])
        elif item.name == "get_delivery_data":
            result = get_delivery_data(args['user_id'])
        else:
            result = "unknown function called"

        function_output.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps({"result":result})
        })

# SECOND LLM CALL 

final_response = client.responses.create(
    model="gpt-5.4-mini",
    input=function_output,
    previous_response_id=response.id
)

print(final_response.output_text)