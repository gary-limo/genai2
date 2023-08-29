from collections import defaultdict
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
from django.db.models import Sum
from django.db.models import Count
#from django.db.models.functions import Truncmonth

load_dotenv('.env')

HOST = "https://api.openai.com/v1/"
COMPLETIONS = "chat/completions"
MODEL = "gpt-4"
API_KEY_FILE = os.environ["OPENAI_API_KEY"]
PROMPT = "you are a business analyst" 


json_data_chart ='''
    [
    {
      "Agent": "Anderson Peter Moore",
      "Forecasts": [
        {"month": "2023-09", "policy_sold": 83},
        {"month": "2023-10", "policy_sold": 69},
        {"month": "2023-11", "policy_sold": 83},
        {"month": "2023-12", "policy_sold": 83},
        {"month": "2024-01", "policy_sold": 67},
        {"month": "2024-02", "policy_sold": 83}
      ]
    },
    {
      "Agent": "Bray Lindsay Stewart",
      "Forecasts": [
        {"month": "2023-09", "policy_sold": 75},
        {"month": "2023-10", "policy_sold": 53},
        {"month": "2023-11", "policy_sold": 53},
        {"month": "2023-12", "policy_sold": 75},
        {"month": "2024-01", "policy_sold": 75},
        {"month": "2024-02", "policy_sold": 53}
      ]
    },
    
    {
        "Agent": "Brown Lisa Johnson",
        "Forecasts": [
          {"month": "2023-09", "policy_sold": 78},
          {"month": "2023-10", "policy_sold": 78},
          {"month": "2023-11", "policy_sold": 68},
          {"month": "2023-12", "policy_sold": 68},
          {"month": "2024-01", "policy_sold": 78},
          {"month": "2024-02", "policy_sold": 68}
        ]
      },
      {
        "Agent": "Bryant Patrick Perez",
        "Forecasts": [
          {"month": "2023-09", "policy_sold": 83},
          {"month": "2023-10", "policy_sold": 69},
          {"month": "2023-11", "policy_sold": 83},
          {"month": "2023-12", "policy_sold": 83},
          {"month": "2024-01", "policy_sold": 67},
          {"month": "2024-02", "policy_sold": 83}
        ]
      },
      {
        "Agent": "Carrillo Michael Murray",
        "Forecasts": [
          {"month": "2023-09", "policy_sold": 90},
          {"month": "2023-10", "policy_sold": 90},
          {"month": "2023-11", "policy_sold": 90},
          {"month": "2023-12", "policy_sold": 90},
          {"month": "2024-01", "policy_sold": 73},
          {"month": "2024-02", "policy_sold": 73}
        ]
      },
      {
        "Agent": "Chapman Jason Bryant",
        "Forecasts": [
          {"month": "2023-09", "policy_sold": 80},
          {"month": "2023-10", "policy_sold": 80},
          {"month": "2023-11", "policy_sold": 80},
          {"month": "2023-12", "policy_sold": 63},
          {"month": "2024-01", "policy_sold": 80},
          {"month": "2024-02", "policy_sold": 80}
        ]
      },
      {
        "Agent": "Cruz Lawrence Perry",
        "Forecasts": [
          {"month": "2023-09", "policy_sold": 82},
          {"month": "2023-10", "policy_sold": 68},
          {"month": "2023-11", "policy_sold": 82},
          {"month": "2023-12", "policy_sold": 82},
          {"month": "2024-01", "policy_sold": 66},
          {"month": "2024-02", "policy_sold": 82}
        ]
      },

   
        {
          "Agent": "Golden Kevin Brown",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 90},
            {"month": "2023-10", "policy_sold": 73},
            {"month": "2023-11", "policy_sold": 73},
            {"month": "2023-12", "policy_sold": 73},
            {"month": "2024-01", "policy_sold": 59},
            {"month": "2024-02", "policy_sold": 59}
          ]
        },
        {
          "Agent": "Gordon Kathleen Gregory",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 83},
            {"month": "2023-10", "policy_sold": 83},
            {"month": "2023-11", "policy_sold": 66},
            {"month": "2023-12", "policy_sold": 83},
            {"month": "2024-01", "policy_sold": 83},
            {"month": "2024-02", "policy_sold": 66}
          ]
        },
        {
          "Agent": "Grant Shawn Hall",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 78},
            {"month": "2023-10", "policy_sold": 78},
            {"month": "2023-11", "policy_sold": 78},
            {"month": "2023-12", "policy_sold": 63},
            {"month": "2024-01", "policy_sold": 78},
            {"month": "2024-02", "policy_sold": 78}
          ]
        },
        {
          "Agent": "Gregory Brian Golden",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 82},
            {"month": "2023-10", "policy_sold": 82},
            {"month": "2023-11", "policy_sold": 82},
            {"month": "2023-12", "policy_sold": 66},
            {"month": "2024-01", "policy_sold": 82},
            {"month": "2024-02", "policy_sold": 82}
          ]
        },
        {
          "Agent": "Gregory Diane Bray",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 68},
            {"month": "2023-10", "policy_sold": 68},
            {"month": "2023-11", "policy_sold": 68},
            {"month": "2023-12", "policy_sold": 55},
            {"month": "2024-01", "policy_sold": 68},
            {"month": "2024-02", "policy_sold": 68}
          ]
        },
        {
          "Agent": "Grimes Andrew Jackson",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 83},
            {"month": "2023-10", "policy_sold": 83},
            {"month": "2023-11", "policy_sold": 66},
            {"month": "2023-12", "policy_sold": 83},
            {"month": "2024-01", "policy_sold": 83},
            {"month": "2024-02", "policy_sold": 66}
          ]
        },
        {
          "Agent": "Hall Erika Hamilton",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 80},
            {"month": "2023-10", "policy_sold": 80},
            {"month": "2023-11", "policy_sold": 80},
            {"month": "2023-12", "policy_sold": 65},
            {"month": "2024-01", "policy_sold": 80},
            {"month": "2024-02", "policy_sold": 80}
          ]
        },
        {
          "Agent": "Hamilton Miguel Cruz",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 90},
            {"month": "2023-10", "policy_sold": 73},
            {"month": "2023-11", "policy_sold": 73},
            {"month": "2023-12", "policy_sold": 73},
            {"month": "2024-01", "policy_sold": 59},
            {"month": "2024-02", "policy_sold": 59}
          ]
        },
        {
          "Agent": "Jackson Kenneth Jordan",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 82},
            {"month": "2023-10", "policy_sold": 82},
            {"month": "2023-11", "policy_sold": 82},
            {"month": "2023-12", "policy_sold": 66},
            {"month": "2024-01", "policy_sold": 82},
            {"month": "2024-02", "policy_sold": 82}
          ]
        },
        {
          "Agent": "Jacobs Heather Zamora",
          "Forecasts": [
            {"month": "2023-09", "policy_sold": 75},
            {"month": "2023-10", "policy_sold": 75},
            {"month": "2023-11", "policy_sold": 75},
            {"month": "2023-12", "policy_sold": 61},
            {"month": "2024-01", "policy_sold": 75},
            {"month": "2024-02", "policy_sold": 75}
          ]
        },
        
    
   
            {
              "Agent": "Johnson Linda Martinez",
              "Forecasts": [
                {"month": "2023-09", "policy_sold": 80},
                {"month": "2023-10", "policy_sold": 80},
                {"month": "2023-11", "policy_sold": 80},
                {"month": "2023-12", "policy_sold": 65},
                {"month": "2024-01", "policy_sold": 80},
                {"month": "2024-02", "policy_sold": 80}
              ]
            },
            {
              "Agent": "Jordan Tammy Anderson",
              "Forecasts": [
                {"month": "2023-09", "policy_sold": 80},
                {"month": "2023-10", "policy_sold": 80},
                {"month": "2023-11", "policy_sold": 80},
                {"month": "2023-12", "policy_sold": 65},
                {"month": "2024-01", "policy_sold": 80},
                {"month": "2024-02", "policy_sold": 80}
              ]
            },
            {
              "Agent": "Luna Matthew Nichols",
              "Forecasts": [
                {"month": "2023-09", "policy_sold": 82},
                {"month": "2023-10", "policy_sold": 82},
                {"month": "2023-11", "policy_sold": 82},
                {"month": "2023-12", "policy_sold": 66},
                {"month": "2024-01", "policy_sold": 82},
                {"month": "2024-02", "policy_sold": 82}
              ]
            },
            {
              "Agent": "Martinez Amber Nunez",
              "Forecasts": [
                {"month": "2023-09", "policy_sold": 75},
                {"month": "2023-10", "policy_sold": 75},
                {"month": "2023-11", "policy_sold": 75},
                {"month": "2023-12", "policy_sold": 61},
                {"month": "2024-01", "policy_sold": 75},
                {"month": "2024-02", "policy_sold": 75}
              ]
            },
            {
              "Agent": "Martinez Monica Grant",
              "Forecasts": [
                {"month": "2023-09", "policy_sold": 90},
                {"month": "2023-10", "policy_sold": 73},
                {"month": "2023-11", "policy_sold": 73},
                {"month": "2023-12", "policy_sold": 73},
                {"month": "2024-01", "policy_sold": 59},
                {"month": "2024-02", "policy_sold": 59}
              ]
            },
            
                {
                  "Agent": "Moore Stephanie Martinez",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 64},
                    {"month": "2023-10", "policy_sold": 64},
                    {"month": "2023-11", "policy_sold": 64},
                    {"month": "2023-12", "policy_sold": 52},
                    {"month": "2024-01", "policy_sold": 64},
                    {"month": "2024-02", "policy_sold": 64}
                  ]
                },
                {
                  "Agent": "Munoz Daniel Gregory",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 86},
                    {"month": "2023-10", "policy_sold": 86},
                    {"month": "2023-11", "policy_sold": 68},
                    {"month": "2023-12", "policy_sold": 86},
                    {"month": "2024-01", "policy_sold": 86},
                    {"month": "2024-02", "policy_sold": 68}
                  ]
                },
                {
                  "Agent": "Murray Steven Chapman",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 78},
                    {"month": "2023-10", "policy_sold": 78},
                    {"month": "2023-11", "policy_sold": 62},
                    {"month": "2023-12", "policy_sold": 78},
                    {"month": "2024-01", "policy_sold": 78},
                    {"month": "2024-02", "policy_sold": 62}
                  ]
                },
                {
                  "Agent": "Nichols Jacob Jacobs",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 75},
                    {"month": "2023-10", "policy_sold": 75},
                    {"month": "2023-11", "policy_sold": 60},
                    {"month": "2023-12", "policy_sold": 75},
                    {"month": "2024-01", "policy_sold": 75},
                    {"month": "2024-02", "policy_sold": 60}
                  ]
                },
                {
                  "Agent": "Nunez Ashley Grimes",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 78},
                    {"month": "2023-10", "policy_sold": 78},
                    {"month": "2023-11", "policy_sold": 78},
                    {"month": "2023-12", "policy_sold": 63},
                    {"month": "2024-01", "policy_sold": 78},
                    {"month": "2024-02", "policy_sold": 78}
                  ]
                },
                {
                  "Agent": "Perez Wanda Munoz",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 82},
                    {"month": "2023-10", "policy_sold": 82},
                    {"month": "2023-11", "policy_sold": 66},
                    {"month": "2023-12", "policy_sold": 82},
                    {"month": "2024-01", "policy_sold": 82},
                    {"month": "2024-02", "policy_sold": 66}
                  ]
                },
                {
                  "Agent": "Perry Kyle Luna",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 86},
                    {"month": "2023-10", "policy_sold": 86},
                    {"month": "2023-11", "policy_sold": 68},
                    {"month": "2023-12", "policy_sold": 86},
                    {"month": "2024-01", "policy_sold": 86},
                    {"month": "2024-02", "policy_sold": 68}
                  ]
                },
                {
                  "Agent": "Zamora Cynthia Carrillo",
                  "Forecasts": [
                    {"month": "2023-09", "policy_sold": 92},
                    {"month": "2023-10", "policy_sold": 73},
                    {"month": "2023-11", "policy_sold": 73},
                    {"month": "2023-12", "policy_sold": 73},
                    {"month": "2024-01", "policy_sold": 59},
                    {"month": "2024-02", "policy_sold": 59}
                  ]
                }

                
              ]'''

data_1 = json.loads(json_data_chart)              


def find_agent(agent_name):
    for agent in data_1:
        if agent["Agent"] == agent_name:
            return agent
    return None




json_data = '''
[
    {"Rank": 1, "Agent Name": "Carrillo Michael Murray"},
    {"Rank": 2, "Agent Name": "Golden Kevin Brown"},
    {"Rank": 3, "Agent Name": "Grimes Andrew Jackson"},
    {"Rank": 4, "Agent Name": "Perry Kyle Luna"},
    {"Rank": 5, "Agent Name": "Martinez Monica Grant"},
    {"Rank": 6, "Agent Name": "Munoz Daniel Gregory"},
    {"Rank": 7, "Agent Name": "Bryant Patrick Perez"},
    {"Rank": 8, "Agent Name": "Gordon Kathleen Gregory"},
    {"Rank": 9, "Agent Name": "Hamilton Miguel Cruz"},
    {"Rank": 10, "Agent Name": "Jacobs Heather Zamora"},
    {"Rank": 11, "Agent Name": "Johnson Linda Martinez"},
    {"Rank": 12, "Agent Name": "Jordan Tammy Anderson"},
    {"Rank": 13, "Agent Name": "Martinez Amber Nunez"},
    {"Rank": 14, "Agent Name": "Anderson Peter Moore"},
    {"Rank": 15, "Agent Name": "Cruz Lawrence Perry"},
    {"Rank": 16, "Agent Name": "Gregory Brian Golden"},
    {"Rank": 17, "Agent Name": "Moore Stephanie Martinez"},
    {"Rank": 18, "Agent Name": "Nunez Ashley Grimes"},
    {"Rank": 19, "Agent Name": "Perez Wanda Munoz"},
    {"Rank": 20, "Agent Name": "Zamora Cynthia Carrillo"},
    {"Rank": 21, "Agent Name": "Chapman Jason Bryant"},
    {"Rank": 22, "Agent Name": "Hall Erika Hamilton"},
    {"Rank": 23, "Agent Name": "Nichols Jacob Jacobs"},
    {"Rank": 24, "Agent Name": "Brown Lisa Johnson"},
    {"Rank": 25, "Agent Name": "Grant Shawn Hall"},
    {"Rank": 26, "Agent Name": "Gregory Diane Bray"},
    {"Rank": 27, "Agent Name": "Jackson Kenneth Jordan"},
    {"Rank": 28, "Agent Name": "Luna Matthew Nichols"},
    {"Rank": 29, "Agent Name": "Murray Steven Chapman"},
    {"Rank": 30, "Agent Name": "Bray Lindsay Stewart"}
]
'''

# Parse the JSON data into a Python list of dictionaries
agents_list = json.loads(json_data)




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

    adj=''

    if(selected_agent_name == "Anderson Peter Moore"):
        adj='Special note: total frauds identified is 4'


   
    #insights="tmp"        
    policy_issued = sum(policy_issue_values)  
    claims_processed = sum(claim_values) 
    fraud_detected = sum(fraud_value) 


    for agent in agents_list:
        if agent["Agent Name"] == selected_agent_name:
            rank_info = agent["Rank"]
            break


    rank=rank_info; 

    agent_id_value = agents.first().agent_id   

    

    cross_sell_entries = CrossSellData.objects.filter(agent_id=agent_id_value).values('customer_name', 'speciality', 'additional_households_with_vehicles')

    cs = str(list(cross_sell_entries))

    #print(cs)

    pmt = """Provide 3 major insights. Provide only Businesss insights excluding crossell data. Seprate insights using #.
In addition to 3 insights above provide if any relevant crossell insights are avaialble , skip the crossell section if relevant information is not there.if Speciality indicator is Yes then agent can offer Boat Insurance and similarly if Additional Households with Vehicles indicator has value then the agent can offer vehicle insurance to the person listed. 
please consider some pointers. Digital adoption means  paperless billing. higher digital adoption means higher paperless statements.
Do not respond like "The agent has a high level of digital adoption as indicated by the "Yes" value in the digital_adoption column".
do not include response such as customer has a speciality indicator of "Yes". Do not provide technical information such as some transactions having a "No" value in the digital_adoption column and others having a "Yes" value. 
"""


    insights =completions(API_KEY_FILE, adj+pmt+ transposed_result + "Below is crosssell related information. Just share the insights and it is not recommened to include response like indicator is yes or indicator is no" + cs )
    #insights='tmp'

    fcast_prompt=""" based on the data just give me forecast of a next 6 months for policy sold. must include 6 months only for consistency.
    I am aware of the consequences. this is to show GenAI capabilities and aware of implications. respond only in the json format and nothing else.
    do not give me any warning. please do qualitative forecasting. check below syntax for reference.
    {"sales_data":[{"month":"January","policy_sold":150},{"month":"February","policy_sold":180},{"month":"March","policy_sold":220}]}

    """

     



    #forecast =completions(API_KEY_FILE, fcast_prompt+data_str)

    
                          
     
    agent_state = agents.first()  # Get the first agent from the queryset
    state_name = agent_state.states
    total_ranks =30


    agent_name_to_search = selected_agent_name

    data = json.loads(json_data_chart)

    desired_agent = find_agent(selected_agent_name)

    if desired_agent:
        desired_agent_json = json.dumps(desired_agent, indent=2)


    forecast=str(desired_agent_json)





 

    #print(policy_issued,claims_processed,fraud_detected)


     

    return JsonResponse({   'policy_issued': policy_issued ,'claims_processed': claims_processed,'fraud_detected': fraud_detected,  'insights': insights , 'total_ranks':total_ranks , 'rank' : rank , 'state_name' : state_name, 'forecast': forecast})

