from django.urls import path 
from configurator import views 

urlpatterns = [
    path("configurator/", views.configurator, name='configurator'),
]