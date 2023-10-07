from django.urls import path, include

from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

import hello.views
from hello import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ask", hello.views.ask, name="ask"),
    path('agency_names', views.agency_names, name='agency_names'),
    path('metrics_data', views.metrics_data, name='metrics_data'),
    path('index.html', TemplateView.as_view(template_name='index.html'), name='index_html'),
    path('users-profile.html', TemplateView.as_view(template_name='users-profile.html'), name='users-profile.html'),
    path('pages-faq.html', TemplateView.as_view(template_name='pages-faq.html'), name='pages-faq.html'),
    path('pages-contact.html', TemplateView.as_view(template_name='pages-contact.html'), name='pages-contact.html'),
 


    
    # Add other URL patterns here
]