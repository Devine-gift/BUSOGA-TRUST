from django.shortcuts import render
from .models import  Projects, Partne

# Create your views here.
def admin(request):
    return render(request, 'hrAdmin/index.html')

def login(request):
    partner_count = Partne.objects.count()
    project_count = Projects.objects.count()
    return render(request, 'hrAdmin/adminDasboard.html', {'partner_count': partner_count,'project_count': project_count})

def Partner(request):
    part = Partne.objects.all()
    return render(request, 'hrAdmin/partners.html', {'part': part})
    

def projects(request):
    proj = Projects.objects.all()
    return render(request, 'hrAdmin/projects.html', {'proj':proj})

def projectview(request):
    proj = Projects.objects.all()
    return render(request, 'hrAdmin/projectview.html', {'proj':proj})

def tasks(request):
    return render(request, 'hrAdmin/tasks.html')

def tasksboard(request):
    return render(request, 'hrAdmin/tasks-board.html')

def partnerlist(request):
     return render(request, 'hrAdmin/partner-list.html')

def partnerprofile(request):
    return render(request, 'hrAdmin/partner-profile.html')

