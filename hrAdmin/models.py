from django.db import models

# Create your models here.
class Partne(models.Model):
    firstname = models.CharField(max_length=50) 
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    interest= models.TextField(max_length=50)
    companyname= models.CharField(max_length=50)
    biodata = models.FileField(upload_to ='partner/pdfs/docx/doc')
    acceptancenote = models.FileField(upload_to = 'partner/pdfs/docx/doc')
    
    
