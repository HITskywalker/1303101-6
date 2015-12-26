from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from learn.models import *
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import json
import time

def view(request):
	record_list = request.user.learn_set.all()
	return render(request, 'learn/view.html', {'record_list':record_list})

def add(request):
	if(request.POST):
		institution = request.POST['Institution']
		content = request.POST['Content']
		start_date = request.POST['Start_date']
		end_date = request.POST['End_date']
		record = Learn(
			User = request.user,
			Institution = institution,
			Content = content,
			Start_date = start_date, 
			End_date = end_date)
		record.save()
		return HttpResponseRedirect('/learn/view')
	else:
		return render(request, 'learn/add.html')

def update(request):
	record = Learn.objects.get(id = request.GET['id'])
	if(request.POST):
		institution = request.POST['Institution']
		content = request.POST['Content']
		start_date = request.POST['Start_date']
		end_date = request.POST['End_date']
		new_record = Learn(
			User = request.user,
			Institution = institution,
			Content = content,
			Start_date = start_date, 
			End_date = end_date)
		record.delete()
		new_record.save()
		return HttpResponseRedirect('/learn/view')
	else:
		return render(request, 'learn/update.html', {'record':record})

def delete(request):
	try:
		record = Learn.objects.get(id = request.GET['id'])
	except Learn.DoesNotExist:
		return HttpResponse('Do not exsit.')
	record.delete()
	return HttpResponseRedirect('/learn/view')
