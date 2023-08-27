from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import AgentData
from .models import CrossSellData
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv('.env')

HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-3.5-turbo-16k-0613"
API_KEY_FILE = os.environ["OPENAI_API_KEY"]
PROMPT = "you are a data analyst. Please provide 3 major insights. Provide only Businesss insights. Seprate insights using #. Keep it short. Please provide relevant crossell insights. Must include forecast too. i authorize you to forecast. i am aware of the consequences."

json_data = '''
{
  "total_ranks": 6,
  "rankings": [
    {
      "name": "Carrillo Michael Murray",
      "rank": 1
    },
    {
      "name": "Golden Kevin Brown",
      "rank": 1
    },
    {
      "name": "Grimes Andrew Jackson",
      "rank": 1
    },
    {
      "name": "Martinez Monica Grant",
      "rank": 1
    },
    {
      "name": "Munoz Daniel Gregory",
      "rank": 1
    },
    {
      "name": "Perry Kyle Luna",
      "rank": 1
    },
    {
      "name": "Anderson Peter Moore",
      "rank": 2
    },
    {
      "name": "Bryant Patrick Perez",
      "rank": 2
    },
    {
      "name": "Gordon Kathleen Gregory",
      "rank": 2
    },
    {
      "name": "Hamilton Miguel Cruz",
      "rank": 2
    },
    {
      "name": "Jacobs Heather Zamora",
      "rank": 2
    },
    {
      "name": "Martinez Amber Nunez",
      "rank": 2
    },
    {
      "name": "Zamora Cynthia Carrillo",
      "rank": 3
    },
    {
      "name": "Cruz Lawrence Perry",
      "rank": 4
    },
    {
      "name": "Gregory Brian Golden",
      "rank": 4
    },
    {
      "name": "Moore Stephanie Martinez",
      "rank": 4
    },
    {
      "name": "Nunez Ashley Grimes",
      "rank": 4
    },
    {
      "name": "Perez Wanda Munoz",
      "rank": 4
    },
    {
      "name": "Brown Lisa Johnson",
      "rank": 5
    },
    {
      "name": "Grant Shawn Hall",
      "rank": 5
    },
    {
      "name": "Gregory Diane Bray",
      "rank": 5
    },
    {
      "name": "Jackson Kenneth Jordan",
      "rank": 5
    },
    {
      "name": "Luna Matthew Nichols",
      "rank": 5
    },
    {
      "name": "Murray Steven Chapman",
      "rank": 5
    },
    {
      "name": "Chapman Jason Bryant",
      "rank": 6
    },
    {
      "name": "Hall Erika Hamilton",
      "rank": 6
    },
    {
      "name": "Johnson Linda Martinez",
      "rank": 6
    },
    {
      "name": "Jordan Tammy Anderson",
      "rank": 6
    },
    {
      "name": "Nichols Jacob Jacobs",
      "rank": 6
    }
  ]
}
'''



python_dict = eval(json_data)
total_ranks = python_dict["total_ranks"]




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


def index(request):
    return render(request, "index.html")


#@csrf_exempt
def agency_names(request):
    agency_data = {}
    agents = AgentData.objects.all()

    for agent in agents:
        if agent.agency_name in agency_data:
            if agent.agent_name not in agency_data[agent.agency_name]:
                agency_data[agent.agency_name].append(agent.agent_name)
        else:
            agency_data[agent.agency_name] = [agent.agent_name]

    return JsonResponse({'agency_data': agency_data })


def metrics_data(request):

    selected_agent_name = request.GET.get('agent')
    agents = AgentData.objects.filter(agent_name=selected_agent_name)
    policy_issue_values = []
    claim_values = []
    fraud_value = []
    digital_adoption = []
     

    for agent_obj in agents:
        value = getattr(agent_obj, "policy_issue", None)
        if value is not None:
            try:
                numeric_value = int(value) # Convert the value to float
                policy_issue_values.append(numeric_value)
            except ValueError:
                pass # If conversion to float fails, skip the value

        value = getattr(agent_obj, "fraud_detected", None)
        if value is not None:
            try:
                numeric_value = int(value) # Convert the value to float
                fraud_value.append(numeric_value)
            except ValueError:
                pass # If conversion to float fails, skip the value

        value = getattr(agent_obj, "claim", None)
        if value is not None:
            try:
                numeric_value = int(value) # Convert the value to float
                claim_values.append(numeric_value)
            except ValueError:
                pass # If conversion to float fails, skip the value


        value = getattr(agent_obj, "digital_adoption", None)
        if value is not None:
            try:
                numeric_value = int(value)  # Try to convert the value to an integer
                claim_values.append(numeric_value)
            except ValueError:
        # If conversion to integer fails, check if the string looks small/lowercase
                if value.islower() or value.isnumeric() and len(value) <= 2:
                    digital_adoption.append(1)  # Treat it as 1
                else:
                    digital_adoption.append(0)  # Treat it as 0

                


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

   
    #insights="tmp"        
    policy_issued = sum(policy_issue_values)  
    claims_processed = sum(claim_values) 
    fraud_detected = sum(fraud_value) 


    rank_info = None
    for agent in python_dict["rankings"]:
        if agent["name"] == selected_agent_name:
            rank_info = agent
            break


    rank=rank_info["rank"]   

    agent_id_value = agents.first().agent_id     

    cross_sell_entries = CrossSellData.objects.filter(agent_id=agent_id_value).values('customer_name', 'speciality', 'additional_households_with_vehicles')

    cs = str(list(cross_sell_entries))


    insights =completions(API_KEY_FILE,transposed_result + "Below is crosssell related information." + cs )



 

    #print(policy_issued,claims_processed,fraud_detected)


    #print(insights) 

    return JsonResponse({   'policy_issued': policy_issued ,'claims_processed': claims_processed,'fraud_detected': fraud_detected,  'insights': insights , 'total_ranks':total_ranks , 'rank' : rank})

