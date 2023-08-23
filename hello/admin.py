from django.contrib import admin

from .models import AgentData
from .models import CrossSellData

admin.site.register(AgentData)
admin.site.register(CrossSellData)
