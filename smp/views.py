from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from smp.models import Paper,Auther,Jounery
from django.template import Context
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import datetime
import time

class PF(forms.Form):
		auther =  forms.CharField()
		jounery = forms.CharField()
		institution = forms.CharField()
		pdf = forms.FileField()

class userform(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())

# Create your views here.
def getDoc(request):
	   if(request.method == "POST"):
	      post = request.POST
	      pf = PF(request.POST,request.FILES)
	      if pf.is_valid():
	      	print pf.cleaned_data["pdf"].name
	        a = Auther(
	            name = pf.cleaned_data["auther"],
	            institution=pf.cleaned_data["institution"]    
	        )
	        j = Jounery(
	            J_name=pf.cleaned_data["jounery"]        
	        )
	        p = Paper(
	            timestamp = time.localtime(time.time()),
	            pdf = pf.cleaned_data["pdf"],
	            pdfname = pf.cleaned_data["pdf"].name
	            )
	        try:
	        	a = Auther.objects.get(name = a.name)
	        except ObjectDoesNotExist:
	        	a.save()
	        try:
	        	j = Jounery.objects.get(J_name = j.J_name)
	        except ObjectDoesNotExist:
	        	j.save()
	        p.save()
	        p.auther.add(a)
	        p.jounery.add(j)
	        p.save()
	        
	        return HttpResponse(
	        '''
	        <html>
	
									<body>
									
										<h1>OK</h1>
									</body>
									
					</html>
	        
	        '''
	        
	        )
	      else:
	        print pf
	        return	 HttpResponse(
	        '''
	        <html>
	
									<body>
									
										<h1>unvaild!</h1>
									</body>
									
					</html>
	        
	        ''')
	   else:
	     pf = PF()
	     return render_to_response("test.html",{"pf":pf})


def ok():
	return HttpResponse(
		 '''
        <html>

								<body>
								
									<h1>OK</h1>
								</body>
								
				</html>
        
        '''
  )
def notvalid():
	return HttpResponse(
			 '''
	        <html>
	
									<body>
									
										<h1>not valid!</h1>
									</body>
									
					</html>
	        
	        '''
			
			)
def ViewPaper(request):
	if (request.GET.get('name',False)):
		Get = request.GET
		au = Auther.objects.get(name = Get["name"])
		if(au):
			p = Paper.objects.filter(auther = au)
			return render_to_response("view.html",{"paper_list":p})
		else:
			return 	 HttpResponse(
	        '''
	        <html>
	
									<body>									
										<h1>Not Found!</h1>
									</body>
									
					</html>
	        
	        ''')
	else:
		p = Paper.objects.filter(auther = au)
		return render_to_response("view.html",{"paper_list":p})


def register(req):
	if(req.method == "POST"):
		uf = userform(req.POST)
		if uf.is_valid():
			user = User.objects.create_user(
				username = uf.cleaned_data["username"],
				password = uf.cleaned_data["password"]
			)
			user.is_staff = True
			return ok()
		else:
			return notvalid()
	else:
		uf = userform()
		return render_to_response("register.html",{"uf":uf})		

def login_view(request):
	if(request.method == "POST"):
		uf = userform(request.POST)
		if(uf.is_valid()):
			print uf.cleaned_data['username'] 
			print uf.cleaned_data['password']
			user = authenticate(username=request.POST['username'], password=request.POST['password'])
		
			if user:
				login(request, user)
				return ok()
			else:
				print 1
				return notvalid()
		else:
			print 2
			return notvalid()
	else:
		uf = userform()
		return render_to_response("Login.html")

def logout_view(request):
    logout(request)
    return ok()

search_choice = ( 
    ('', u"---------"), 
    (1, u"pdfname"),         
    (2, u"author"),         
    (3, u"jounery"), 
    (4, u"institution"), 
) 

class searchform(forms.Form):
	text = forms.CharField(label = u"search",required = True)
	choice = forms.ChoiceField(label= (u"you choice"),required=True, choices=search_choice)


def Search(request):
	dic = {1:"pdfname",2:"auther",3:"jounery",4:"institution"}
	if(request.method == "POST"):
		back_list = {}
		post = request.POST
		sf = searchform(post)
		if(sf.is_valid()):
			cho = sf.cleaned_data['choice']
			print sf.cleaned_data['choice']
			print cho == 1
			if(cho == '1'):
				#print cho
				back_list = Paper.objects.filter(pdfname = sf.cleaned_data['text'])
			if(cho =='2'):
				au = Auther.objects.get(name = sf.cleaned_data['text'])
				if(not au):
					return notvalid()
				back_list = Paper.objects.filter(auther = au)
			if(cho =='3'):
				jo = Jounery.objects.get(J_name = sf.cleaned_data['text'])
				if(not jo):
					return notvalid()
				back_list = Paper.objects.filter(jounery = jo)
			if(cho =='4'):
				au = Auther.objects.filter(institution = sf.cleaned_data['text'])
				if(not au):
					return notvalid()
				for i in au:
					if(not back_list):
						back_list = Paper.objects.filter(auther = au)
					back_list = back_list | Paper.objects.filter(auther = au)
			return render_to_response("view.html",{"paper_list":back_list})
		else:
			notvalid()
	else:
		sf = searchform()
		return render_to_response("search.html",{"uf":sf})




def dele(req):
	if(req.method == "GET" and  req.GET['id']):
		g = req.GET
		pap = Paper.objects.get(id = g['id'])
		if(pap):
			pap.delete()
			return ok()
		return notvalid()