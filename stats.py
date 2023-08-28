from collections import defaultdict
from django.db.models import Sum
import os 
import django
# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData  # Import your AgentData model

# Query the database to get the policy issued count, claim count, and fraud detected count for each agent
agent_data = AgentData.objects.values('agent_name').annotate(
    policy_issued=Sum('policy_issue'),
    claim_count=Sum('claim'),
    fraud_detected_count=Sum('fraud_detected')
)

# Create a dictionary to store agent data
agent_info = defaultdict(dict)
for item in agent_data:
    agent_name = item['agent_name']
    agent_info[agent_name]['policy_issued'] = item['policy_issued']
    agent_info[agent_name]['claim_count'] = item['claim_count']
    agent_info[agent_name]['fraud_detected_count'] = item['fraud_detected_count']

# Print the agent information nicely
for agent_name, info in agent_info.items():
    print(f"Agent Name: {agent_name}")
    print(f"Policy Issued: {info['policy_issued']}")
    print(f"Claim Count: {info['claim_count']}")
    print(f"Fraud Detected Count: {info['fraud_detected_count']}")
    print("=" * 20)
