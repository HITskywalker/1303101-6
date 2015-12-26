# coding:utf-8
from django.contrib import admin
from .models import Project,Member

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','project_num','source')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Project,ProjectAdmin)
admin.site.register(Member,MemberAdmin)


