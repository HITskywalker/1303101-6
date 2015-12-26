# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from smp.models import Paper, Auther, Jounery, Prize,zzauthor,zhuanzhu,prauthor,zhuanli,zlauthor
from django.template import Context
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import json
import time


class AF(forms.Form):
    auther = forms.CharField()
    institution = forms.CharField()


class PF(forms.Form):
    auther = forms.CharField()
    jounery = forms.CharField()
    institution = forms.CharField()
    pdf = forms.FileField()


class userform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


def ok():
    return render_to_response("ok.html")


def notvalid():
    return render_to_response("notvalid.html")


# Create your views here.
def getDoc(request):
    if (request.method == "POST" and request.user is not None):
        post = request.POST
        usert = request.user
        pf = PF(request.POST, request.FILES)
        if pf.is_valid():
            print pf.cleaned_data["pdf"].name
            a = Auther(
                name=pf.cleaned_data["auther"],
                institution=pf.cleaned_data["institution"]
            )
            j = Jounery(
                J_name=pf.cleaned_data["jounery"]
            )
            p = Paper(
                user=usert,
                timestamp=time.localtime(time.time()),
                pdf=pf.cleaned_data["pdf"],
                pdfname=pf.cleaned_data["pdf"].name
            )
            try:
                a = Auther.objects.get(name=a.name)
            except ObjectDoesNotExist:
                a.save()
            try:
                j = Jounery.objects.get(J_name=j.J_name)
            except ObjectDoesNotExist:
                j.save()
            p.jounery = j
            p.save()
            p.MauthorID = a.id
            p.auther.add(a)
            p.save()

            return ok()
        else:
            print pf
            return notvalid()
    else:
        return render(request, "upload.html")


def ViewPaper(request):
    dic = {}
    dic['state'] = "0"
    if (request.GET.get('username', False)):
        Get = request.GET
        try:
            usert = User.objects.get(username=Get["username"])
            p = Paper.objects.filter(user=usert)
            if (request.user.is_authenticated()):
                print request.user
                dic['state'] = "1"
            else:
                dic['state'] = '0'
            return render_to_response("view.html", {"paper_list": p, "dic": json.dumps(dic)})
        except ObjectDoesNotExist:
            return notvalid()
    else:
        p = Paper.objects.all()
        return render_to_response("view.html", {"paper_list": p, "dic": json.dumps(dic)})


def register(req):
    if (req.method == "POST"):
        uf = userform(req.POST)
        if uf.is_valid():
            user = User.objects.create_user(
                username=uf.cleaned_data["username"],
                password=uf.cleaned_data["password"]
            )
            user.is_staff = True
            user.save()
            user = authenticate(
                username=uf.cleaned_data["username"],
                password=uf.cleaned_data["password"]
            )
            login(req, user)
            addprauthor(req)
            addzzauthor(req)
            addzlauthor(req)
            return ok()
        else:
            return notvalid()
    else:
        return render(req, "register.html")


def login_view(request):
    if (request.method == "POST"):
        uf = userform(request.POST)
        if (uf.is_valid()):
            print uf.cleaned_data['username']
            print uf.cleaned_data['password']
            user = authenticate(username=request.POST['username'], password=request.POST['password'])

            if user:
                login(request, user)
                # response.set_cookie("is_login","1")
                print request.user
                List = {}
                List['state'] = "True"
                List["message"] = "OK!"
                List['name'] = user.username
                response = render(request, 'login.html', {'List': json.dumps(List)})
                response.set_cookie('is_log', 1, 3600)
                response.set_cookie('username', user.username, 3600)
                return response
            else:
                print 1
                List = {}
                List['state'] = "False"
                List["message"] = "password wrong!"
                List['name'] = ""
                return render(request, 'login.html', {'List': json.dumps(List)})
        else:
            print 2
            return notvalid()
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    response = ok()
    response.delete_cookie('is_log')
    response.delete_cookie('username')
    return response


search_choice = (
    ('', u"---------"),
    (1, u"pdfname"),
    (2, u"author"),
    (3, u"jounery"),
    (4, u"institution"),
)


class searchform(forms.Form):
    text = forms.CharField(label=u"search", required=True)
    choice = forms.ChoiceField(label=(u"you choice"), required=True, choices=search_choice)


def Search(request):
    dic = {1: "pdfname", 2: "auther", 3: "jounery", 4: "institution"}
    if (request.method == "POST"):
        back_list = {}
        post = request.POST
        sf = searchform(post)
        if (sf.is_valid()):
            cho = sf.cleaned_data['choice']
            print sf.cleaned_data['choice']
            print cho == 1
            if (cho == '1'):
                # print cho
                back_list = Paper.objects.filter(pdfname=sf.cleaned_data['text'])
            if (cho == '2'):
                au = Auther.objects.get(name=sf.cleaned_data['text'])
                if (not au):
                    return notvalid()
                back_list = Paper.objects.filter(auther=au)
            if (cho == '3'):
                jo = Jounery.objects.get(J_name=sf.cleaned_data['text'])
                if (not jo):
                    return notvalid()
                back_list = Paper.objects.filter(jounery=jo)
            if (cho == '4'):
                au = Auther.objects.filter(institution=sf.cleaned_data['text'])
                if (not au):
                    return notvalid()
                for i in au:
                    if (not back_list):
                        back_list = Paper.objects.filter(auther=au)
                    back_list = back_list | Paper.objects.filter(auther=au)
            return render_to_response("view.html", {"paper_list": back_list})
        else:
            notvalid()
    else:
        return render(request, "search.html")


def showp(req):
    if (req.method == "GET" and req.GET.get('id', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['id'])
        print pap.pdfname
        return render_to_response("detail.html", {"paper": pap})
    return notvalid()


def dele(req):
    if (req.method == "GET" and req.GET.get('id', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['id'])
        if (pap and pap.user == req.user):
            pap.delete()
            return ok()
        return notvalid()
    return notvalid()


def change(req):
    if (req.method == "GET" and req.GET.get('id', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['id'])
        if (pap and pap.user == req.user):
            au = Auther.objects.get(id=pap.MauthorID)
            # pap.delete()
            return render_to_response("change.html", {"paper": pap, "au": au})
    elif (req.method == "POST" and req.GET.get('id', False)):
        g = req.GET
        pf = PF(req.POST, req.FILES)
        try:
            pap = Paper.objects.get(id=g['id'])
            au = Auther.objects.get(id=pap.MauthorID)
        except ObjectDoesNotExist:
            return notvalid()
        pap.auther.remove(au)
        if (pf.is_valid()):
            a = Auther(
                name=pf.cleaned_data["auther"],
                institution=pf.cleaned_data["institution"]
            )
            j = Jounery(
                J_name=pf.cleaned_data["jounery"]
            )
            try:
                a = Auther.objects.get(name=a.name)
            except ObjectDoesNotExist:
                a.save()
            try:
                j = Jounery.objects.get(J_name=j.J_name)
            except ObjectDoesNotExist:
                j.save()
            pap.jounery = j
            pap.pdf = pf.cleaned_data["pdf"]
            pap.pdfname = pf.cleaned_data["pdf"].name
            pap.MauthorID = a.id
            pap.auther.add(a)
            pap.save()
            return ok()
        else:
            return notvalid()
    else:
        return notvalid()


def addauthor(req):
    if (req.method == "GET" and req.GET.get('id', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['id'])
        if (pap and pap.user == req.user):
            af = AF()
            return render(req, "addauthor.html")
    elif (req.method == "POST"):
        g = req.GET
        pap = Paper.objects.get(id=g['id'])
        af = AF(req.POST)
        if (af.is_valid()):
            a = Auther(
                name=af.cleaned_data["auther"],
                institution=af.cleaned_data["institution"]
            )
            try:
                a = Auther.objects.get(name=a.name)
            except ObjectDoesNotExist:
                a.save()
            pap.auther.add(a)
            pap.save()
            return ok()
    else:
        return notvalid()


def changeau(req):
    if (req.method == "POST" and req.GET.get('Aid', False) and req.GET.get('Pid', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['Pid'])
        au = Auther.objects.get(id=g['Aid'])
        aid = au.id
        pap.auther.remove(au)
        af = AF(req.POST)
        if (af.is_valid()):
            a = Auther(
                name=af.cleaned_data["auther"],
                institution=af.cleaned_data["institution"]
            )
            try:
                a = Auther.objects.get(name=a.name)
            except ObjectDoesNotExist:
                a.save()
            pap.auther.add(a)
            if (pap.MauthorID == aid):
                pap.MauthorID = a.id
            pap.save()
            return ok()
        else:
            return notvalid()
    elif (req.method == "GET" and req.GET.get('Aid', False) and req.GET.get('Pid', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['Pid'])
        au = Auther.objects.get(id=g['Aid'])
        return render_to_response("changeauthor.html", {"au": au})
        return notvalid()
    return notvalid()


def delau(req):
    if (req.method == "GET" and req.GET.get('Aid', False) and req.GET.get('Pid', False)):
        g = req.GET
        pap = Paper.objects.get(id=g['Pid'])
        au = Auther.objects.get(id=g['Aid'])
        if (not (pap.MauthorID == au.id) and pap and pap.user == req.user):
            pap.auther.remove(au)
            pap.save()
            return ok()
        return notvalid()
    return notvalid()


def sta(req):
    j = Jounery.objects.all()
    for i in j:
        i.jcount = i.paper_set.count()
        if (i.jcount == 0):
            i.delete()
        else:
            i.save()
    a = Auther.objects.all()
    for i in a:
        i.acount = i.paper_set.count()
        print i.paper_set.count()
        if (i.acount == 0):
            i.delete()
        else:
            i.save()
    pnum = Paper.objects.all().count()
    js = Jounery.objects.order_by("jcount")[:5]
    categories = [str(b.J_name) for b in js]
    data = [int(b.jcount) for b in js]
    ans,ans1,ans2,point,point1,point2 = staaa(req)
    points = point+point1+point2
    print data
    print categories
    return render_to_response("static.html", {"jnum": j.count(), "anum": a.count(), "pnum": pnum, 'user': 'hehe',
                                              'categories': categories, 'data': data,'ans':ans,"ans1":ans1,"ans2":ans2,"point":point,"point1":point1,"point2":point2,"points":points})


def index(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact2.html')


def about(request):
    return render(request, 'about2.html')


def show(request):
    return render(request, 'show.html')


# def forgotPassword(request):
#     return render(request,'forgot-pass.html')
def getview(request):
    return render(request, 'view.html')


def tr(req):
    return render(req, "detail.html")

def addprauthor(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf1.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		if(zf.is_valid()):
			z = prauthor(
			name =zf.cleaned_data['name'],
			user = req.user
			)
			try:
				z.save()
			except:
				return notvalid()
			print z.user.username
			return ok()
		return notvalid()
def addprau(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		zid = req.GET['zid']
		if(zf.is_valid()):
			qset = prauthor.objects.filter(name = zf.cleaned_data['name'])
			response = render(req, 'viewzlau.html', {'au_list': qset})
			response.set_cookie('zid',zid, 3600)
			return response


def addprau2(req):
	if(req.method == "GET"):
		auid = req.GET['auid']
		zlau = prauthor.objects.get(id =auid)
		zid = req.COOKIES['zid']
		z = Prize.objects.get(id = zid)
		choice = z.user.count() + 1
		print choice
		if choice == 2:
			zl = z.secondclass.user
			z.secondclass = zlau
		if choice == 3:
			zl = z.thirdclass.user
			z.thirdclass = zlau
		if choice == 4:
			zl = z.fourthclass.user
			z.fourthclass = zlau
		if choice == 5:
			zl = z.fifthclass.user
			z.fifthclass = zlau
		if (choice == 6):
			return notvalid()
		if(not zl.username  == "anou"):
			z.user.remove(zl)
		z.user.add(zlau.user)
		z.save()
		return ok()
	else:
		notvalid()

def countpr(req):
	uset = req.user
	ans = {}
	point = 0
	zl = uset.prauthor
	ans['first'] = zl.first.count()
	ans['second'] = zl.second.count()
	ans['third'] = zl.third.count()
	ans['fourth'] = zl.fourth.count()
	ans['fifth'] = zl.fifth.count()
	for i in zl.first.all():
		if(i.cate == 1):
			point = point + 500
		if(i.cate == 2):
			point = point + 150
		if(i.cate == 3):
			point = point + 100
		if(i.cate == 4):
			point = point + 80
		if(i.cate == 5):
			point = point + 50
	for i in zl.second.all():
		if(i.cate == 1):
			point = point + 500*0.9
		if(i.cate == 2):
			point = point + 150*0.9
		if(i.cate == 3):
			point = point + 100*0.9
		if(i.cate == 4):
			point = point + 80*0.9
		if(i.cate == 5):
			point = point + 50*0.9
	for i in zl.third.all():
		if(i.cate == 1):
			point = point + 500*0.8
		if(i.cate == 2):
			point = point + 150*0.8
		if(i.cate == 3):
			point = point + 100*0.8
		if(i.cate == 4):
			point = point + 80*0.8
		if(i.cate == 5):
			point = point + 50*0.8
	for i in zl.fourth.all():
		if(i.cate == 1):
			point = point + 500*0.7
		if(i.cate == 2):
			point = point + 150*0.7
		if(i.cate == 3):
			point = point + 100*0.7
		if(i.cate == 4):
			point = point + 80*0.7
		if(i.cate == 5):
			point = point + 50*0.7
	return ans,point
def Price(request):
    level_list = [u'国际级', u'国家级', u'省级', u'校级', u'其他']
    prize_list = [u'一等奖', u'二等奖', u'三等奖', u'其他']
    usert = request.user
    status = False
    if request.POST:
        pname = request.POST['prize_name']
        pdate = request.POST['prize_date']
        plevel = request.POST['level']
        if plevel == u'其他':
            plevel = request.POST['level_other']
        pprize = request.POST['prize']
        if pprize == u'其他':
            pprize = request.POST['prize_other']
        z = Prize(name=pname, level=plevel, rank=pprize, \
                         gaintime=datetime.datetime.strptime(pdate, '%Y-%m-%d').date())
        #change here
        if(plevel == u"国家级" and pprize == u"一等奖"):
            z.cate =1
        if(plevel == u"国家级" and pprize == u"二等奖"):
            z.cate =2
        if(plevel == u"国家级" and pprize == u"三等奖"):
            z.cate =3
        if(plevel == u"省级级" and pprize == u"一等奖"):
            z.cate =4
        print plevel == u"国家级" and pprize == u"二等奖"
        print z.cate
        useq = User.objects.get_or_create(username='anou')[0]
        print useq
        z.firstclass = prauthor.objects.get(user = request.user)
        z.secondclass = prauthor.objects.get_or_create(user = useq,name = "")[0]
        z.thirdclass = prauthor.objects.get_or_create(user = useq,name = "")[0]
        z.fourthclass = prauthor.objects.get_or_create(user = useq,name = "")[0]
        z.fifthclass = prauthor.objects.get_or_create(user = useq,name = "")[0]
        allprize = Prize.objects.all()
        flag = False
        for oldprize in allprize:
            if oldprize == z:
                status = -1
                flag = True
                break
        if not flag:
            z.save()
            z.user.add(request.user)
            z.save()
            status = True
    content = {'level_list': level_list, 'prize_list': prize_list, 'status': status}
    return render(request, 'addprice.html', content)

def prizeshow(req):
	if(req.user.is_authenticated()):
		uset = req.user
		allprize = Prize.objects.filter(user=uset)
		return render_to_response("prizeshow.html",{"all":allprize})
	else:
		return notvalid()

def prizedele(req):
	if(req.user.is_authenticated()):
		if(req.GET.get('id', False)):
			pid = req.GET['id']
			prize = Prize.objects.get(id = pid)
			if (prize.user == req.user):
				prize.delete()
				return ok()
			else:
				return notvalid()
		else:
			return notvalid()
	else:
		return notvalid()

def SearchP(request):
    level_list = ['国际级', '国家级', '省级', '校级', '其他']
    prize_list = ['一等奖', '二等奖', '三等奖', '其他']
    if (request.method == "POST"):
        back_list = {}
        post = request.POST
        sf = searchform(post)
        if (sf.is_valid()):
            cho = sf.cleaned_data['choice']
            print sf.cleaned_data['choice']
            print cho == 1
            if (cho == '1'):
                # print cho
                back_list = Prize.objects.filter(name=sf.cleaned_data['text'])
            if (cho == '2'):
                back_list = Prize.objects.filter(level = sf.cleaned_data['text'])
            if (cho == '3'):
                back_list = Prize.objects.filter(rank=sf.cleaned_data['text'])
            return render_to_response("prizeshow.html", {"all": back_list})
        else:
            notvalid()
    else:
        return render(request, "searchp.html")

def changeprize(req):
	level_list = [u'国际级', u'国家级', u'省级', u'校级', u'其他']
	prize_list = [u'一等奖', u'二等奖', u'三等奖', u'其他']
	if(req.method == "GET"):
		if(req.GET.get('id', False)):
			pid = req.GET['id']
			prize = Prize.objects.get(id = pid)
			for level in level_list:
				
				print 1 
			content = {'level_list': level_list, 'prize_list': prize_list,"prize":prize}
			return render(req,"changeprice.html",content)
		else:
			return notvalid()
	else:
		if(req.GET.get('id', False)):
			pid = req.GET['id']
			prize = Prize.objects.get(id = pid)
			if (req.user in prize.user.all()):
				prize.delete()
				Price(req)
				return ok()
			else:
				return notvalid()
		else:
			return notvalid()

class zlaf(forms.Form):
	name = forms.CharField(max_length=30)
class zlf(forms.Form):
    name = forms.CharField(max_length=100)
    number = forms.IntegerField()
    institution = forms.CharField(max_length=30)
    cate = forms.IntegerField()
    gaintime = forms.DateField()
def countzl(req):
	uset = req.user
	ans = {}
	point = 0
	zl = uset.zlauthor
	ans['first'] = zl.first.count()
	ans['second'] = zl.second.count()
	ans['third'] = zl.third.count()
	ans['fourth'] = zl.fourth.count()
	ans['fifth'] = zl.fifth.count()
	for i in zl.first.all():
		if(i.cate == 1):
			point = point + 30
		if(i.cate == 2):
			point = point + 15
		if(i.cate == 3):
			point = point + 10
		if(i.cate == 4):
			point = point + 5
	for i in zl.second.all():
		if(i.cate == 1):
			point = point + 30*0.6
		if(i.cate == 2):
			point = point + 15*0.6
		if(i.cate == 3):
			point = point + 10*0.6
		if(i.cate == 4):
			point = point + 5*0.6
	for i in zl.third.all():
		if(i.cate == 1):
			point = point + 30*0.3
		if(i.cate == 2):
			point = point + 15*0.3
		if(i.cate == 3):
			point = point + 10*0.3
		if(i.cate == 4):
			point = point + 5*0.3
	for i in zl.fourth.all():
		if(i.cate == 1):
			point = point + 30*0.1
		if(i.cate == 2):
			point = point + 15*0.1
		if(i.cate == 3):
			point = point + 10*0.1
		if(i.cate == 4):
			point = point + 5*0.1
	return ans,point
def addzlauthor(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf1.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		if(zf.is_valid()):
			z = zlauthor(
			name =zf.cleaned_data['name'],
			user = req.user
			)
			try:
				z.save()
			except:
				return notvalid()
			print z.user.username
			return ok()
		return notvalid()

def changezl(req):
	if(req.method == "GET"):
		zid = req.GET['zid']
		z = zhuanli.objects.get(id= zid)
		return render_to_response("addzlaf.html",{"paper":z})
	else:
		post = req.POST
		zid = req.GET['zid']
		z = zhuanli.objects.get(id= zid)
		z.name =post['name']
		z.cate =post['cate']
		z.number =post['number']
		z.institution =post['institution']
		z.gaintime =post['gaintime']
		z.save()
		return ok()
def addzl(req):
	if(req.method == "GET"):
		zf = zlf()
		return render_to_response("addzlaf.html",{"zf":zf})
	else:
		zf = zlf(req.POST)
		if(zf.is_valid()):
			z = zhuanli(
			name =zf.cleaned_data['name'],
			number =zf.cleaned_data['number'],
			institution =zf.cleaned_data['institution'],
			cate =zf.cleaned_data['cate'],
			gaintime =zf.cleaned_data['gaintime']
			)
			useq = User.objects.get_or_create(username='anou')[0]
			print useq
			z.firstclass = zlauthor.objects.get(user = req.user)
			z.secondclass = zlauthor.objects.get_or_create(user = useq,name = "")[0]
			z.thirdclass = zlauthor.objects.get_or_create(user = useq,name = "")[0]
			z.fourthclass = zlauthor.objects.get_or_create(user = useq,name = "")[0]
			z.fifthclass = zlauthor.objects.get_or_create(user = useq,name = "")[0]
			z.save()
			z.user.add(req.user)
			z.save()
			return ok()
		return notvalid()

def addzlau(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf1.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		zid = req.GET['zid']
		if(zf.is_valid()):
			qset = zlauthor.objects.filter(name = zf.cleaned_data['name'])
			response = render(req, 'viewzlau.html', {'au_list': qset})
			response.set_cookie('zid',zid, 3600)
			return response


def addzlau2(req):
	if(req.method == "GET"):
		auid = req.GET['auid']
		zlau = zlauthor.objects.get(id =auid)
		zid = req.COOKIES['zid']
		z = zhuanli.objects.get(id = zid)
		choice = z.user.count() + 1
		print choice
		if choice == 2:
			zl = z.secondclass.user
			z.secondclass = zlau
		if choice == 3:
			zl = z.thirdclass.user
			z.thirdclass = zlau
		if choice == 4:
			zl = z.fourthclass.user
			z.fourthclass = zlau
		if choice == 5:
			zl = z.fifthclass.user
			z.fifthclass = zlau
		if (choice == 6):
			return notvalid()
		if(not zl.username  == "anou"):
			z.user.remove(zl)
		z.user.add(zlau.user)
		z.save()
		return ok()
	else:
		notvalid()

def viewzhuanli(req):
	uset = req.user
	qset =uset.zhuanli_set.all()
	return render(req, 'viewzhuanli.html', {'paper_list': qset})

def delezhuanli(req):
	zid = req.GET['zid']
	zhuanli.objects.get(id = zid).delete()
	return ok()

class zzf(forms.Form):
    name = forms.CharField(max_length=100)
    institution = forms.CharField(max_length=30)
    gaintime = forms.DateField()

def countzz(req):
	uset = req.user
	ans = {}
	point = 0
	zl = uset.zzauthor
	ans['first'] = zl.first.count()
	ans['second'] = zl.second.count()
	ans['third'] = zl.third.count()
	ans['fourth'] = zl.fourth.count()
	ans['fifth'] = zl.fifth.count()
	point = ans['first']*50 + ans['second']*0.6*50+ ans['third']*0.3*50+ ans['fourth']*0.1*50
	return ans,point
def addzzauthor(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf1.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		if(zf.is_valid()):
			z = zzauthor(
			name =zf.cleaned_data['name'],
			user = req.user
			)
			try:
				z.save()
			except:
				return notvalid()
			print z.user.username
			addzlauthor(req)
			addprauthor(req)
			return ok()
		return notvalid()
def changezz(req):
	if(req.method == "GET"):
		zid = req.GET['zid']
		z = zhuanzhu.objects.get(id= zid)
		return render_to_response("addzzaf.html",{"paper":z})
	else:
		post = req.POST
		zid = req.GET['zid']
		z = zhuanzhu.objects.get(id= zid)
		z.name =post['name']
		z.institution =post['institution']
		z.gaintime =post['gaintime']
		z.save()
		return ok()
def addzz(req):
	if(req.method == "GET"):
		zf = zzf()
		return render_to_response("addzzaf.html",{"zf":zf})
	else:
		zf = zzf(req.POST)
		if(zf.is_valid()):
			z = zhuanzhu(
			name =zf.cleaned_data['name'],
			institution =zf.cleaned_data['institution'],
			gaintime =zf.cleaned_data['gaintime']
			)
			useq = User.objects.get_or_create(username='anou')[0]
			print useq
			z.firstclass = zzauthor.objects.get(user = req.user)
			z.secondclass = zzauthor.objects.get_or_create(user = useq,name = "")[0]
			z.thirdclass = zzauthor.objects.get_or_create(user = useq,name = "")[0]
			z.fourthclass = zzauthor.objects.get_or_create(user = useq,name = "")[0]
			z.fifthclass = zzauthor.objects.get_or_create(user = useq,name = "")[0]
			z.save()
			z.user.add(req.user)
			z.save()
			return ok()
		return notvalid()

def addzzau(req):
	if(req.method == "GET"):
		zf = zlaf()
		return render_to_response("addzlaf1.html",{"zf":zf})
	else:
		zf = zlaf(req.POST)
		zid = req.GET['zid']
		if(zf.is_valid()):
			qset = zzauthor.objects.filter(name = zf.cleaned_data['name'])
			response = render(req, 'viewzzau.html', {'au_list': qset})
			response.set_cookie('zid',zid, 3600)
			return response

def addzzau2(req):
	if(req.method == "GET"):
		auid = req.GET['auid']
		zlau = zzauthor.objects.get(id =auid)
		zid = req.COOKIES['zid']
		z = zhuanzhu.objects.get(id = zid)
		choice = z.user.count() + 1
		print choice
		if choice == 2:
			zl = z.secondclass.user
			z.secondclass = zlau
		if choice == 3:
			zl = z.thirdclass.user
			z.thirdclass = zlau
		if choice == 4:
			zl = z.fourthclass.user
			z.fourthclass = zlau
		if choice == 5:
			zl = z.fifthclass.user
			z.fifthclass = zlau
		if (choice == 6):
			return notvalid()
		if(not zl.username  == "anou"):
			z.user.remove(zl)
		z.user.add(zlau.user)
		z.save()
		return ok()
	else:
		notvalid()

def viewzhuanzhu(req):
	uset = req.user
	qset =uset.zhuanzhu_set.all()
	return render(req, 'viewzhuanzhu.html', {'paper_list': qset})

def delezhuanzhu(req):
	zid = req.GET['zid']
	zhuanzhu.objects.get(id = zid).delete()
	return ok()

def staaa(req):
	ans,point = countzz(req)
	ans1,point1 = countzl(req)
	ans2,point2 = countpr(req)
	return ans,ans1,ans2,point,point1,point2
"""
def changezl(req):
	if(req.method == "GET"):
		zid = req.GET['zid']
		z = zhuanli.objects.get(id= zid)
		#return render_to_response()
	else:
		post = req.POST
		zid = req.GET['zid']
		z = zhuanli.objects.get(id= zid)
		z.name =post['name']
		z.number =post['number']
		z.institution =post['institution']
		z.gaintime =post['gaintime']
		z.save()
		return ok()
"""
