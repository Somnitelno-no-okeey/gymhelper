from django.urls import path 
from user import views 

urlpatterns = [
    path("auth/", views.auth, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path("profile/", views.profile, name='profile'),
]