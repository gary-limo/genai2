from django.urls import path, include

from django.contrib import admin


admin.autodiscover()

import hello.views
from hello import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ask", hello.views.ask, name="ask"),
    path('agency_names', views.agency_names, name='agency_names'),
    path('metrics_data', views.metrics_data, name='metrics_data'),
 


    
    # Add other URL patterns here
]