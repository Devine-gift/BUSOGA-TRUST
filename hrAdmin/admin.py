from django.contrib import admin

# Register your models here.
from .models import Partne,Projects, Program

admin.site.register(Partne)
admin.site.register(Projects)
admin.site.register(Program)
