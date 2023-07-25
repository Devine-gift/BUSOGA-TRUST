
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.admin, name='admin'),
    path('adminDashboard', views.login, name='login'),
    path('partners', views.Partner, name ='Partner'),
    path('projects', views.projects, name ='projects'),
    path('tasks', views.Partner, name ='tasks'),
    path('tasksboard', views.Partner, name ='tasksboard'),
     path('partner-list', views.partnerlist, name ='partnerlist'),
     path('partner-profile', views.partnerprofile, name ='partnerprofile'),
    
]