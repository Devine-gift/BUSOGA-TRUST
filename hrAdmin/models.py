from django.db import models
from datetime import datetime, date

# Create your models here.
class Partne(models.Model):
    firstname = models.CharField(max_length=50) 
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    interest= models.TextField(max_length=100)
    companyname= models.CharField(max_length=50)
    biodata = models.FileField(upload_to ='partner/pdfs/docx/doc')
    acceptancenote = models.FileField(upload_to = 'partner/pdfs/docx/doc')
    
    
class Projects(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=1000)
    objectives = models.TextField(max_length=1000)
    program = models.TextField(max_length= 1000)
    pam = models.TextField(max_length= 100)
    employees = models.TextField(max_length= 1000)
    startdate = models.DateTimeField(auto_now_add= False, auto_now= False, blank=True)
    endperiod = models.DateTimeField(auto_now_add= False, auto_now=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add= True, auto_now= False, blank=True)
    tasks = models.TextField(max_length=1000)
    
  
class Program(models.Model):
    name = models.CharField(max_length=50)
    districts = models.TextField(max_length= 100)   
    employees = models.TextField(max_length=100)
    project =   models.DateTimeField(max_length=100)
    