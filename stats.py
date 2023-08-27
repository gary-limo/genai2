from collections import defaultdict
from django.db.models import Sum
import os 
import django
# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData  # Import your AgentData model

# Query the database to get the policy issued count for each agent
policy_issued_by_agent = AgentData.objects.values('agent_name').annotate(policy_issued=Sum('policy_issue'))

# Create a dictionary to store agent names and policy issued counts
policy_issued_data = defaultdict(int)
for item in policy_issued_by_agent:
    agent_name = item['agent_name']
    policy_issued = item['policy_issued']
    policy_issued_data[agent_name] = policy_issued



print(dict(policy_issued_data))
