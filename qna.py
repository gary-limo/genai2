from collections import defaultdict
import django
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()
import json 
from hello.models import AgentData
from hello.models import CrossSellData
from dotenv import load_dotenv

import requests
 
#from django.db.models.functions import Truncmonth




load_dotenv('.env')

HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-4"
API_KEY_FILE = os.environ["OPENAI_API_KEY"]
PROMPT = "you are a business analyst" 


def completions(API_KEY_FILE, prompt):
    headers = {
        "Content-Type": "application/json",

        "Authorization": f"Bearer {API_KEY_FILE}",
    }

    data = {
        "model": MODEL,
        #"temperature": 0.1,
      
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
    


selected_agent_name="Anderson Peter Moore"

agents = AgentData.objects.filter(agent_name=selected_agent_name)

transposed_data = []
keys = agents[0].__dict__.keys()
transposed_data.append("|".join(keys))
 
for agent_obj in agents:
    agent_values = []
    for key in keys:
            if key != "_state":
                value = str(getattr(agent_obj, key))
                agent_values.append(value)
    transposed_data.append("|".join(agent_values))
 
transposed_result = "\n".join(transposed_data)
transposed_result = transposed_result.replace("_state|", "")

print(transposed_result)


user_input = input("Enter your text: ")

insights =completions(API_KEY_FILE,transposed_result+ user_input)

print(insights)