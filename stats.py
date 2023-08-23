from dotenv import load_dotenv
import os
import django
import requests
import json
from getpass import getpass
import json
import re
import time



# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData

# Use load_env to trace the path of .env:
load_dotenv('.env')

HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-3.5-turbo-16k-0613"
PROMPT = "you are a data analyst. please calculate the sum of all numbers located under column number 6. always return just a number and nothing else."
API_KEY_FILE = os.environ["OPENAI_API_KEY"]


# Extract only numbers from a string
def extract_numbers(s):
    return float(re.sub(r"[^\d]", "", s))



def create_batches(data, batch_size=20):
    # Handle the first batch separately
    yield data[:batch_size]
    
    # Now, start the loop from after the first batch, and always prepend the column info
    for i in range(batch_size, len(data), batch_size-1):  # Subtract 1 to account for the column info record
        yield [data[0]] + data[i:i+batch_size-1]





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
     
  


policy_issue_values = []

for agent_obj in agents:
    value = getattr(agent_obj, "policy_issue", None)
    if value is not None:
        try:
            numeric_value = int(value) # Convert the value to float
            policy_issue_values.append(numeric_value)
        except ValueError:
            pass # If conversion to float fails, skip the value

# Compute the sum of all policy_issue values
total_sum = sum(policy_issue_values)

print(f"Total Sum: {total_sum}")

