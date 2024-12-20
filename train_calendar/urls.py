from django.urls import path 
from train_calendar import views 

urlpatterns = [
    path("calendar/", views.calendar, name='calendar'),
]