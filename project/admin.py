# coding:utf-8
from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','project_num','source')

admin.site.register(Project,ProjectAdmin)


