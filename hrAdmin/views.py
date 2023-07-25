from django.shortcuts import render
from django.http import HttpResponse
from .forms import partnerform
from .models import Partne

# Create your views here.
def admin(request):
    return render(request, 'hrAdmin/index.html')

def login(request):
    partner_count = Partne.objects.count()
    return render(request, 'hrAdmin/adminDasboard.html', {'partner_count': partner_count})

def Partner(request):
    part = Partne.objects.all()
    return render(request, 'hrAdmin/partners.html', {'part': part})
    

def projects(request):
    return render(request, 'hrAdmin/projects.html')

def tasks(request):
    return render(request, 'hrAdmin/tasks.html')

def tasksboard(request):
    return render(request, 'hrAdmin/tasks-board.html')

def partnerlist(request):
     return render(request, 'hrAdmin/partner-list.html')

def partnerprofile(request):
    return render(request, 'hrAdmin/partner-profile.html')

