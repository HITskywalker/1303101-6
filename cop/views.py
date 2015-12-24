from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from cop.models import *
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import json
import time

def view(request):
	cop_list = Cop.objects.all()
	return render(request, 'cop/view.html', {'cop_list':cop_list})

def add(request):
	if(request.POST):
		member_names = []
		catagory = request.POST['catagory']
		p_num = request.POST['p_num']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		place = request.POST['place']
		purpose = request.POST['purpose']
		report_name = request.POST['report_name']
		report_url = request.POST['report_url']
		save_report = request.POST['save_report']
		save_photo = request.POST['save_photo']
		for i in range(int(p_num)):
			member_names.append(request.POST['member_name'+str(i)])
		member_list = []
		for i in range(int(p_num)):
			try:
				member = People.objects.get(name = member_names[i])
			except People.DoesNotExist:
				member = People(name = member_names[i])
				member.save()
			member_list.append(member)
		record = Cop(
			catagory = catagory,
			owner = request.user,
			p_num = p_num,
			start_date = start_date,
			end_date = end_date,
			place = place,
			purpose = purpose,
			report_name = report_name,
			report_url = report_url,
			save_report = save_report,
			save_photo = save_photo)
		record.save()
		for i in range(int(p_num)):
			record.member.add(member_list[i])
		record.save()
		return HttpResponseRedirect('/cop/view/')
	else:
		return render(request, 'cop/add.html')

def update(request, cop_id):
	cop = Cop.objects.get(id = cop_id)
	if(request.POST):
		member_names = []
		catagory = request.POST['catagory']
		p_num = request.POST['p_num']
		start_date = request.POST['start_date']
		end_date = request.POST['end_date']
		place = request.POST['place']
		purpose = request.POST['purpose']
		report_name = request.POST['report_name']
		report_url = request.POST['report_url']
		save_report = request.POST['save_report']
		save_photo = request.POST['save_photo']
		for i in range(int(p_num)):
			member_names.append(request.POST['member_name'+str(i)])
		member_list = []
		for i in range(int(p_num)):
			try:
				member = People.objects.get(name = member_names[i])
			except People.DoesNotExist:
				member = People(name = member_names[i])
				member.save()
			member_list.append(member)
		new_record = Cop(
			catagory = catagory,
			owner = request.user,
			p_num = p_num,
			start_date = start_date,
			end_date = end_date,
			place = place,
			purpose = purpose,
			report_name = report_name,
			report_url = report_url,
			save_report = save_report,
			save_photo = save_photo)
		cop.delete()
		new_record.save()
		for i in range(int(p_num)):
			new_record.member.add(member_list[i])
		new_record.save()
		return HttpResponseRedirect('/cop/view')
	else:
		p = cop.member.all()
		member = [i.name for i in p]
		return render(request, 'cop/update.html', 
			{'cop':cop, 'member':json.dumps(member)})

def delete(request):
	try:
		cop = Cop.objects.get(id = request.GET['id'])
	except Cop.DoesNotExist:
		return HttpResponse('Do not exsit.')
	cop.delete()
	return HttpResponseRedirect('/cop/view')