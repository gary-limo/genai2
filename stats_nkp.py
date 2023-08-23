from dotenv import load_dotenv
import os
import django
import requests
import json
from getpass import getpass
import json



# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData

# Use load_env to trace the path of .env:
load_dotenv('.env')

HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-3.5-turbo-16k-0613"
PROMPT = "you are a mathematician. please calculate the sum of all numbers located under policy_issue column"
API_KEY_FILE = os.environ["OPENAI_API_KEY"]



def completions(API_KEY_FILE, prompt):
    headers = {
        "Content-Type": "application/json",

        "Authorization": f"Bearer {API_KEY_FILE}",
    }

    data = {
        "model": MODEL,
        "temperature": 0,
        "messages": [{"role": "system", "content": PROMPT}, {"role": "user", "content": prompt}],
    }

    response = requests.post(HOST + COMPLETIONS, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_json = response.json()
        reply = response_json["choices"][0]["message"]["content"]
        return reply.strip()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return ""


    

agents = AgentData.objects.filter(agent_name="Gregory Brian Golden")
     
  

transposed_data = []

# Extract keys from the first agent object to use as column names
keys = agents[0].__dict__.keys()

# Add keys as the first row in transposed data
transposed_data.append("|".join(keys))

# Iterate through each agent object
for agent_obj in agents:
    agent_values = []
    for key in keys:
        if key != "_state":
            value = str(getattr(agent_obj, key))
            agent_values.append(value)
    transposed_data.append("|".join(agent_values))

# Join transposed data rows with line breaks
transposed_result = "\n".join(transposed_data)
transposed_result = transposed_result.replace("_state|", "")

# Print the transposed result
reply =completions(API_KEY_FILE,transposed_result)

print(reply)
#print(transposed_result)

    
