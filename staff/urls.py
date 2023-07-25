
from django.urls import path
from . import views
urlpatterns = [
    
    path('stafflogin', views.stafflogin, name='stafflogin'),
    path('register',views.register, name ='register' ),
    path('staff-dashboard', views.staffdashboard, name='staffdashboard')
    
]


