from django.db import models

class AgentData(models.Model):
    agency_name = models.CharField(max_length=100)
    agent_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    transaction_date = models.DateField()
    policy_issue = models.CharField(max_length=50)
    digital_adoption = models.CharField(max_length=20)
    product_type = models.CharField(max_length=50)
    claim = models.CharField(max_length=20)
    states = models.CharField(max_length=50)
    commision = models.IntegerField()
    fraud_detected = models.IntegerField()

    def __str__(self):
        return str(self.agent_id)  # You can change this to a meaningful representation

class CrossSellData(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    agent_id = models.IntegerField()
    speciality = models.CharField(max_length=50)
    additional_households_with_vehicles = models.CharField(max_length=20)

    def __str__(self):
        return str(self.customer_id)  # You can change this to a meaningful representation
