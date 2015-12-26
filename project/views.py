# coding: utf-8

from django import forms
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
import json
# app specific files

from .models import *
from .forms import *

def create_project2(request):
    Mem = Member.objects.all()
    name = []
    age = []
    for i in range(len(Mem)):
        name.append(Mem[i].name)
        age.append(Mem[i].age)
    if(request.POST):
        names = request.POST['nameid']
        member_names = names.split(',')
        try:
            instance = Project.objects.get(project_num=int(request.POST['project_num']))
            return HttpResponse("Already Exists")
        except Project.DoesNotExist:
            instance = Project(
                name = request.POST['project_name'],
                project_num=int(request.POST['project_num']),
                source= request.POST['source'],
                person= request.POST['person'],
                bund= request.POST['bund'],
                start_time= request.POST['start_time'],
                end_time= request.POST['end_time']
            )
            instance.save()
            for i in range(len(member_names)):
                tmpmem = Member.objects.get_or_create(id=member_names[i])
                instance.project_member.add(Member.objects.get(id=int(member_names[i])))
            instance.save()
            return HttpResponse('OK')
    else:
        return render(request,'project/create_project.html',{'name':json.dumps(name),'age':json.dumps(age)})

def list_project(request):
  
    list_items = Project.objects.all()
    paginator = Paginator(list_items ,10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('project/list_project.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def view_project(request, id):
    instance = Project.objects.get(id = id)
    pname = instance.name
    team=[]
    for item in instance.project_member.all():
        team.append(item.name)
    t=get_template('project/view_project.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_project(request, id):

    project_instance = Project.objects.get(id=id)

    form = ProjectForm(request.POST or None, instance = project_instance)

    if form.is_valid():
        form.save()

    t=get_template('project/edit_project.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
def create_projectidentify(request):
    form = ProjectIdentifyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectIdentifyForm()

    t = get_template('project/create_projectidentify.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_projectidentify2(request,id):
    p_instance = Project.objects.get(id=id)
    pi_instance = ProjectIdentify(
        name=p_instance.name,
        project_num=p_instance.project_num,
        source=p_instance.source,
        person=p_instance.person,
        bund=p_instance.bund,
        start_time=p_instance.start_time,
        end_time=p_instance.end_time,
        identify_time='',
        identify_org='',
        identify_text=''
    )
    form = ProjectIdentifyForm(request.POST or None, instance = pi_instance)
    if form.is_valid():
        form.save()
        form = ProjectIdentifyForm()

    t = get_template('project/create_projectidentify.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_projectidentify(request):
  
    list_items = ProjectIdentify.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('project/list_projectidentify.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_projectidentify(request, id):
    projectidentify_instance = ProjectIdentify.objects.get(id = id)

    t=get_template('project/view_projectidentify.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_projectidentify(request, id):

    projectidentify_instance = ProjectIdentify.objects.get(id=id)

    form = ProjectIdentifyForm(request.POST or None, instance = projectidentify_instance)

    if form.is_valid():
        form.save()

    t=get_template('project/edit_projectidentify.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_projectcheck(request):
    form = ProjectCheckForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProjectCheckForm()

    t = get_template('project/create_projectcheck.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_projectcheck2(request,id):
    p_instance = Project.objects.get(id=id)
    pc_instance = ProjectCheck(
        name=p_instance.name,
        project_num=p_instance.project_num,
        source=p_instance.source,
        person=p_instance.person,
        bund=p_instance.bund,
        start_time=p_instance.start_time,
        end_time=p_instance.end_time,
        check_time='',
        check_org='',
        check_text=''
    )
    form = ProjectCheckForm(request.POST or None, instance = pc_instance)
    if form.is_valid():
        form.save()
        form = ProjectCheckForm()

    t = get_template('project/create_projectcheck.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

def list_projectcheck(request):
  
    list_items = ProjectCheck.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('project/list_projectcheck.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_projectcheck(request, id):
    projectcheck_instance = ProjectCheck.objects.get(id = id)

    t=get_template('project/view_projectcheck.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_projectcheck(request, id):

    projectcheck_instance = ProjectCheck.objects.get(id=id)
    form = ProjectCheckForm(request.POST or None, instance = projectcheck_instance)
    if form.is_valid():
        form.save()
    t=get_template('project/edit_projectcheck.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def create_member(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MemberForm()

    t = get_template('project/create_member.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_member(request):

    list_items = Member.objects.all()
    paginator = Paginator(list_items ,10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('project/list_member.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def edit_member(request, id):

    member_instance = Member.objects.get(id=id)

    form = MemberForm(request.POST or None, instance = member_instance)

    if form.is_valid():
        form.save()

    t=get_template('project/edit_member.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))