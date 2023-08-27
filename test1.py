import json 


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

# Parse the JSON data into a Python dictionary
python_dict = eval(json_data)

# Print the Python dictionary
total_ranks = python_dict["total_ranks"]
print("Total Ranks:", total_ranks)

# Name to search for
search_name = "Carrillo Michael Murray"

# Find rank information based on the search_name
rank_info = None
for agent in python_dict["rankings"]:
    if agent["name"] == search_name:
        rank_info = agent
        break

# If the agent was found
if rank_info:
    print("Name:", rank_info["name"])
    print("Rank:", rank_info["rank"])
else:
    print(f"Agent '{search_name}' not found.")
