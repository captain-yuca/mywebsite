from django.contrib import admin
from django.contrib import admin
from myProfile import models

# Register your models here.
from .models import Project, AboutInfo, AboutUpToInfo, HomeInfo, Blog, Category

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','title', 'description', 'image', 'redirect_url')

admin.site.register(Project, ProjectAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('description', 'image')

admin.site.register(AboutInfo, AboutAdmin)

class UpToAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(AboutUpToInfo, UpToAdmin )

class HomeAdmin(admin.ModelAdmin):
    list_display = ('header', 'subheader', 'cv')

admin.site.register(HomeInfo, HomeAdmin)

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
