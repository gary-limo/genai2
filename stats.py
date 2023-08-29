from collections import defaultdict
from django.db.models import Sum
import os 
import django

# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData  # Import your AgentData model

# Query the database to get the policy issued count for each agent
agent_data = AgentData.objects.values('agent_name').annotate(
    policy_issued=Sum('policy_issue')
)

# Create a dictionary to store agent data
agent_info = defaultdict(dict)
for item in agent_data:
    agent_name = item['agent_name']
    agent_info[agent_name]['policy_issued'] = item['policy_issued']

# Print the agent information without using a for loop
agent_names = agent_info.keys()
agent_names_str = "\n".join([f"Agent Name: {name}\nPolicy Issued: {agent_info[name]['policy_issued']}\n{'=' * 20}" for name in agent_names])
print(agent_names_str)
