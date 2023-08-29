import json

json_data_chart ='''
    [
    {
      "Agent": "Anderson Peter Moore",
      "Forecasts": [
        {"Month": "2023-09", "Policies Sold": 83},
        {"Month": "2023-10", "Policies Sold": 69},
        {"Month": "2023-11", "Policies Sold": 83},
        {"Month": "2023-12", "Policies Sold": 83},
        {"Month": "2024-01", "Policies Sold": 67},
        {"Month": "2024-02", "Policies Sold": 83}
      ]
    },
    {
      "Agent": "Bray Lindsay Stewart",
      "Forecasts": [
        {"Month": "2023-09", "Policies Sold": 75},
        {"Month": "2023-10", "Policies Sold": 53},
        {"Month": "2023-11", "Policies Sold": 53},
        {"Month": "2023-12", "Policies Sold": 75},
        {"Month": "2024-01", "Policies Sold": 75},
        {"Month": "2024-02", "Policies Sold": 53}
      ]
    },
    
    {
        "Agent": "Brown Lisa Johnson",
        "Forecasts": [
          {"Month": "2023-09", "Policies Sold": 78},
          {"Month": "2023-10", "Policies Sold": 78},
          {"Month": "2023-11", "Policies Sold": 68},
          {"Month": "2023-12", "Policies Sold": 68},
          {"Month": "2024-01", "Policies Sold": 78},
          {"Month": "2024-02", "Policies Sold": 68}
        ]
      },
      {
        "Agent": "Bryant Patrick Perez",
        "Forecasts": [
          {"Month": "2023-09", "Policies Sold": 83},
          {"Month": "2023-10", "Policies Sold": 69},
          {"Month": "2023-11", "Policies Sold": 83},
          {"Month": "2023-12", "Policies Sold": 83},
          {"Month": "2024-01", "Policies Sold": 67},
          {"Month": "2024-02", "Policies Sold": 83}
        ]
      },
      {
        "Agent": "Carrillo Michael Murray",
        "Forecasts": [
          {"Month": "2023-09", "Policies Sold": 90},
          {"Month": "2023-10", "Policies Sold": 90},
          {"Month": "2023-11", "Policies Sold": 90},
          {"Month": "2023-12", "Policies Sold": 90},
          {"Month": "2024-01", "Policies Sold": 73},
          {"Month": "2024-02", "Policies Sold": 73}
        ]
      },
      {
        "Agent": "Chapman Jason Bryant",
        "Forecasts": [
          {"Month": "2023-09", "Policies Sold": 80},
          {"Month": "2023-10", "Policies Sold": 80},
          {"Month": "2023-11", "Policies Sold": 80},
          {"Month": "2023-12", "Policies Sold": 63},
          {"Month": "2024-01", "Policies Sold": 80},
          {"Month": "2024-02", "Policies Sold": 80}
        ]
      },
      {
        "Agent": "Cruz Lawrence Perry",
        "Forecasts": [
          {"Month": "2023-09", "Policies Sold": 82},
          {"Month": "2023-10", "Policies Sold": 68},
          {"Month": "2023-11", "Policies Sold": 82},
          {"Month": "2023-12", "Policies Sold": 82},
          {"Month": "2024-01", "Policies Sold": 66},
          {"Month": "2024-02", "Policies Sold": 82}
        ]
      },

   
        {
          "Agent": "Golden Kevin Brown",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 90},
            {"Month": "2023-10", "Policies Sold": 73},
            {"Month": "2023-11", "Policies Sold": 73},
            {"Month": "2023-12", "Policies Sold": 73},
            {"Month": "2024-01", "Policies Sold": 59},
            {"Month": "2024-02", "Policies Sold": 59}
          ]
        },
        {
          "Agent": "Gordon Kathleen Gregory",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 83},
            {"Month": "2023-10", "Policies Sold": 83},
            {"Month": "2023-11", "Policies Sold": 66},
            {"Month": "2023-12", "Policies Sold": 83},
            {"Month": "2024-01", "Policies Sold": 83},
            {"Month": "2024-02", "Policies Sold": 66}
          ]
        },
        {
          "Agent": "Grant Shawn Hall",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 78},
            {"Month": "2023-10", "Policies Sold": 78},
            {"Month": "2023-11", "Policies Sold": 78},
            {"Month": "2023-12", "Policies Sold": 63},
            {"Month": "2024-01", "Policies Sold": 78},
            {"Month": "2024-02", "Policies Sold": 78}
          ]
        },
        {
          "Agent": "Gregory Brian Golden",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 82},
            {"Month": "2023-10", "Policies Sold": 82},
            {"Month": "2023-11", "Policies Sold": 82},
            {"Month": "2023-12", "Policies Sold": 66},
            {"Month": "2024-01", "Policies Sold": 82},
            {"Month": "2024-02", "Policies Sold": 82}
          ]
        },
        {
          "Agent": "Gregory Diane Bray",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 68},
            {"Month": "2023-10", "Policies Sold": 68},
            {"Month": "2023-11", "Policies Sold": 68},
            {"Month": "2023-12", "Policies Sold": 55},
            {"Month": "2024-01", "Policies Sold": 68},
            {"Month": "2024-02", "Policies Sold": 68}
          ]
        },
        {
          "Agent": "Grimes Andrew Jackson",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 83},
            {"Month": "2023-10", "Policies Sold": 83},
            {"Month": "2023-11", "Policies Sold": 66},
            {"Month": "2023-12", "Policies Sold": 83},
            {"Month": "2024-01", "Policies Sold": 83},
            {"Month": "2024-02", "Policies Sold": 66}
          ]
        },
        {
          "Agent": "Hall Erika Hamilton",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 80},
            {"Month": "2023-10", "Policies Sold": 80},
            {"Month": "2023-11", "Policies Sold": 80},
            {"Month": "2023-12", "Policies Sold": 65},
            {"Month": "2024-01", "Policies Sold": 80},
            {"Month": "2024-02", "Policies Sold": 80}
          ]
        },
        {
          "Agent": "Hamilton Miguel Cruz",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 90},
            {"Month": "2023-10", "Policies Sold": 73},
            {"Month": "2023-11", "Policies Sold": 73},
            {"Month": "2023-12", "Policies Sold": 73},
            {"Month": "2024-01", "Policies Sold": 59},
            {"Month": "2024-02", "Policies Sold": 59}
          ]
        },
        {
          "Agent": "Jackson Kenneth Jordan",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 82},
            {"Month": "2023-10", "Policies Sold": 82},
            {"Month": "2023-11", "Policies Sold": 82},
            {"Month": "2023-12", "Policies Sold": 66},
            {"Month": "2024-01", "Policies Sold": 82},
            {"Month": "2024-02", "Policies Sold": 82}
          ]
        },
        {
          "Agent": "Jacobs Heather Zamora",
          "Forecasts": [
            {"Month": "2023-09", "Policies Sold": 75},
            {"Month": "2023-10", "Policies Sold": 75},
            {"Month": "2023-11", "Policies Sold": 75},
            {"Month": "2023-12", "Policies Sold": 61},
            {"Month": "2024-01", "Policies Sold": 75},
            {"Month": "2024-02", "Policies Sold": 75}
          ]
        },
        
    
   
            {
              "Agent": "Johnson Linda Martinez",
              "Forecasts": [
                {"Month": "2023-09", "Policies Sold": 80},
                {"Month": "2023-10", "Policies Sold": 80},
                {"Month": "2023-11", "Policies Sold": 80},
                {"Month": "2023-12", "Policies Sold": 65},
                {"Month": "2024-01", "Policies Sold": 80},
                {"Month": "2024-02", "Policies Sold": 80}
              ]
            },
            {
              "Agent": "Jordan Tammy Anderson",
              "Forecasts": [
                {"Month": "2023-09", "Policies Sold": 80},
                {"Month": "2023-10", "Policies Sold": 80},
                {"Month": "2023-11", "Policies Sold": 80},
                {"Month": "2023-12", "Policies Sold": 65},
                {"Month": "2024-01", "Policies Sold": 80},
                {"Month": "2024-02", "Policies Sold": 80}
              ]
            },
            {
              "Agent": "Luna Matthew Nichols",
              "Forecasts": [
                {"Month": "2023-09", "Policies Sold": 82},
                {"Month": "2023-10", "Policies Sold": 82},
                {"Month": "2023-11", "Policies Sold": 82},
                {"Month": "2023-12", "Policies Sold": 66},
                {"Month": "2024-01", "Policies Sold": 82},
                {"Month": "2024-02", "Policies Sold": 82}
              ]
            },
            {
              "Agent": "Martinez Amber Nunez",
              "Forecasts": [
                {"Month": "2023-09", "Policies Sold": 75},
                {"Month": "2023-10", "Policies Sold": 75},
                {"Month": "2023-11", "Policies Sold": 75},
                {"Month": "2023-12", "Policies Sold": 61},
                {"Month": "2024-01", "Policies Sold": 75},
                {"Month": "2024-02", "Policies Sold": 75}
              ]
            },
            {
              "Agent": "Martinez Monica Grant",
              "Forecasts": [
                {"Month": "2023-09", "Policies Sold": 90},
                {"Month": "2023-10", "Policies Sold": 73},
                {"Month": "2023-11", "Policies Sold": 73},
                {"Month": "2023-12", "Policies Sold": 73},
                {"Month": "2024-01", "Policies Sold": 59},
                {"Month": "2024-02", "Policies Sold": 59}
              ]
            },
            
                {
                  "Agent": "Moore Stephanie Martinez",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 64},
                    {"Month": "2023-10", "Policies Sold": 64},
                    {"Month": "2023-11", "Policies Sold": 64},
                    {"Month": "2023-12", "Policies Sold": 52},
                    {"Month": "2024-01", "Policies Sold": 64},
                    {"Month": "2024-02", "Policies Sold": 64}
                  ]
                },
                {
                  "Agent": "Munoz Daniel Gregory",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 86},
                    {"Month": "2023-10", "Policies Sold": 86},
                    {"Month": "2023-11", "Policies Sold": 68},
                    {"Month": "2023-12", "Policies Sold": 86},
                    {"Month": "2024-01", "Policies Sold": 86},
                    {"Month": "2024-02", "Policies Sold": 68}
                  ]
                },
                {
                  "Agent": "Murray Steven Chapman",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 78},
                    {"Month": "2023-10", "Policies Sold": 78},
                    {"Month": "2023-11", "Policies Sold": 62},
                    {"Month": "2023-12", "Policies Sold": 78},
                    {"Month": "2024-01", "Policies Sold": 78},
                    {"Month": "2024-02", "Policies Sold": 62}
                  ]
                },
                {
                  "Agent": "Nichols Jacob Jacobs",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 75},
                    {"Month": "2023-10", "Policies Sold": 75},
                    {"Month": "2023-11", "Policies Sold": 60},
                    {"Month": "2023-12", "Policies Sold": 75},
                    {"Month": "2024-01", "Policies Sold": 75},
                    {"Month": "2024-02", "Policies Sold": 60}
                  ]
                },
                {
                  "Agent": "Nunez Ashley Grimes",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 78},
                    {"Month": "2023-10", "Policies Sold": 78},
                    {"Month": "2023-11", "Policies Sold": 78},
                    {"Month": "2023-12", "Policies Sold": 63},
                    {"Month": "2024-01", "Policies Sold": 78},
                    {"Month": "2024-02", "Policies Sold": 78}
                  ]
                },
                {
                  "Agent": "Perez Wanda Munoz",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 82},
                    {"Month": "2023-10", "Policies Sold": 82},
                    {"Month": "2023-11", "Policies Sold": 66},
                    {"Month": "2023-12", "Policies Sold": 82},
                    {"Month": "2024-01", "Policies Sold": 82},
                    {"Month": "2024-02", "Policies Sold": 66}
                  ]
                },
                {
                  "Agent": "Perry Kyle Luna",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 86},
                    {"Month": "2023-10", "Policies Sold": 86},
                    {"Month": "2023-11", "Policies Sold": 68},
                    {"Month": "2023-12", "Policies Sold": 86},
                    {"Month": "2024-01", "Policies Sold": 86},
                    {"Month": "2024-02", "Policies Sold": 68}
                  ]
                },
                {
                  "Agent": "Zamora Cynthia Carrillo",
                  "Forecasts": [
                    {"Month": "2023-09", "Policies Sold": 92},
                    {"Month": "2023-10", "Policies Sold": 73},
                    {"Month": "2023-11", "Policies Sold": 73},
                    {"Month": "2023-12", "Policies Sold": 73},
                    {"Month": "2024-01", "Policies Sold": 59},
                    {"Month": "2024-02", "Policies Sold": 59}
                  ]
                }

                
              ]'''
                     

data = json.loads(json_data_chart)

def find_agent(agent_name):
    for agent in data:
        if agent["Agent"] == agent_name:
            return agent
    return None

# Provide the agent name you're interested in
desired_agent_name = "Zamora Cynthia Carrillo"

desired_agent = find_agent(desired_agent_name)

if desired_agent:
    desired_agent_json = json.dumps(desired_agent, indent=2)
    print(desired_agent_json)
else:
    print(f"Agent '{desired_agent_name}' not found in the data.")
