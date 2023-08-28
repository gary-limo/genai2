import json

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

# Name to search for
search_name = "Carrillo Michael Murray"

# Find the rank based on the agent name
for agent in agents_list:
    if agent["Agent Name"] == search_name:
        rank_info = agent["Rank"]
        break

# Print the rank information
print(f"The rank for {search_name} is {rank_info}")
