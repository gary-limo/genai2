from collections import defaultdict
from django.db.models import Sum, Count, Func, F
from django.db.models.functions import ExtractMonth
import os 
import django

# Set the environment variable to your Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hello.settings")
django.setup()

from hello.models import AgentData  # Import your AgentData model

# Define a dictionary to map month numbers to month names
month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

# Get a list of all unique agent names
unique_agent_names = AgentData.objects.values('agent_name').distinct()

# Create a dictionary to store monthly data for each agent
agent_monthly_data = defaultdict(dict)

# Calculate policies sold each month by each agent and populate the agent_monthly_data dictionary
for agent_name_obj in unique_agent_names:
    agent_name = agent_name_obj['agent_name']
    monthly_policies = AgentData.objects.filter(agent_name=agent_name).annotate(
        month=ExtractMonth('transaction_date')
    ).values('month').annotate(
        policies_sold=Sum('policy_issue')
    ).order_by('month')
    
    for item in monthly_policies:
        month_num = item['month']
        policies_sold = item['policies_sold']
        agent_monthly_data[agent_name][month_num] = policies_sold

# Calculate each agent's best and worst month
agent_best_month = {}
agent_worst_month = {}

for agent_name, monthly_data in agent_monthly_data.items():
    best_month = max(monthly_data, key=monthly_data.get)
    worst_month = min(monthly_data, key=monthly_data.get)
    
    agent_best_month[agent_name] = best_month
    agent_worst_month[agent_name] = worst_month

# Calculate combined metrics for each agent
combined_metrics = AgentData.objects.values('agent_name').annotate(
    policy_issued=Sum('policy_issue'),
    total_commission=Sum('commision'),
    total_claims=Sum('claim'),
    total_fraud=Sum('fraud_detected')
)

# Create a dictionary to store the combined metrics for each agent
agent_combined_metrics = {}

for item in combined_metrics:
    agent_name = item['agent_name']
    agent_combined_metrics[agent_name] = {
        'policy_issued': item['policy_issued'],
        'total_commission': item['total_commission'],
        'total_claims': item['total_claims'],
        'total_fraud': item['total_fraud']
    }

# Processing metrics and integrate with monthly data
agent_names_str = ""
for agent_name in unique_agent_names:
    agent_name = agent_name['agent_name']
    agent_info = agent_combined_metrics.get(agent_name, {})
    
    agent_names_str += (
        f"{agent_name}\n"
        f"Policy Issued: {agent_info.get('policy_issued', 0)}\n"
        f"Total Commission: {agent_info.get('total_commission', 0)}\n"
        f"Total Claims: {agent_info.get('total_claims', 0)}\n"
        f"Total Fraud Detected: {agent_info.get('total_fraud', 0)}\n"
        f"Monthly Policies Sold:\n"
    )

    for month_num, policies_sold in agent_monthly_data[agent_name].items():
        month_name = month_names.get(month_num, 'Unknown')
        agent_names_str += f"{month_name}: {policies_sold}\n"
    
    best_month = agent_best_month.get(agent_name, 'Unknown')
    worst_month = agent_worst_month.get(agent_name, 'Unknown')
    
    agent_names_str += (
        f"Best Month: {month_names.get(best_month, 'Unknown')} with {agent_monthly_data[agent_name].get(best_month, 0)} policies sold.\n"
        f"Worst Month: {month_names.get(worst_month, 'Unknown')} with {agent_monthly_data[agent_name].get(worst_month, 0)} policies sold.\n"
        f"{'=' * 5}\n"
    )

print(agent_names_str)
