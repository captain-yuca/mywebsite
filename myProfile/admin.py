from django.contrib import admin
from django.contrib import admin
from myProfile import models

# Register your models here.
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','title', 'description', 'image_url', 'redirect_url')

admin.site.register(Project, ProjectAdmin)
