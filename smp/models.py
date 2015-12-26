#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
        
class Auther(models.Model):
    name = models.CharField(max_length= 30)
    institution = models.CharField(max_length= 30)
    acount = models.IntegerField(default = 0)
    
class Jounery(models.Model):
    J_name=models.CharField(max_length =30)
    jcount = models.IntegerField(default = 0)


class Paper(models.Model):
    user = models. ForeignKey(User)
    MauthorID = models.IntegerField(default = 0)
    auther =  models.ManyToManyField(Auther)
    jounery = models.ForeignKey(Jounery)
    timestamp = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to = './smp/static/upload') 
    pdfname = models.CharField(max_length = 30)
class prauthor(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)

class Prize(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=40)
    #change here
    cate = models.IntegerField(default = 5)
    rank = models.CharField(max_length=10)
    gaintime = models.DateField()
    firstclass = models.ForeignKey(prauthor,related_name="first")
    secondclass = models.ForeignKey(prauthor,related_name="second")
    thirdclass = models.ForeignKey(prauthor,related_name="third")
    fourthclass = models.ForeignKey(prauthor,related_name="fourth")
    fifthclass = models.ForeignKey(prauthor,related_name="fifth")
    def __repr__(self):
        return unicode(self.user)

    def __eq__(self, other):
        return self.user == other.user and self.name == other.name and self.level == other.level and\
               self.rank == other.rank and self.gaintime == other.gaintime

class zlauthor(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)

class zhuanli(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    cate = models.IntegerField()
    number = models.IntegerField()
    institution = models.CharField(max_length=30)
    gaintime = models.DateField()
    firstclass = models.ForeignKey(zlauthor,related_name="first")
    secondclass = models.ForeignKey(zlauthor,related_name="second")
    thirdclass = models.ForeignKey(zlauthor,related_name="third")
    fourthclass = models.ForeignKey(zlauthor,related_name="fourth")
    fifthclass = models.ForeignKey(zlauthor,related_name="fifth")

class zzauthor(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)

class zhuanzhu(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=30)
    gaintime = models.DateField()
    firstclass = models.ForeignKey(zzauthor,related_name="first")
    secondclass = models.ForeignKey(zzauthor,related_name="second")
    thirdclass = models.ForeignKey(zzauthor,related_name="third")
    fourthclass = models.ForeignKey(zzauthor,related_name="fourth")
    fifthclass = models.ForeignKey(zzauthor,related_name="fifth")
"""
class zzauthor(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)
	firstcount = models.IntegerField(default = 0)
	secondcount = models.IntegerField(default = 0)
	thirdcount = models.IntegerField(default = 0)
	fourthcount = models.IntegerField(default = 0)
	fifthcount = models.IntegerField(default = 0)

class zhuanzhu(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    public = models.CharField(max_length=30)
    gaintime = models.DateField()
    firstclass = models.IntegerField(default = 0)
    firstname = models.CharField(max_length=30)
    secondclass = models.IntegerField(default = 0)
    secondname = models.CharField(max_length=30)
    thirdclass = models.IntegerField(default = 0)
    thirdname = models.CharField(max_length=30)
    fourthclass = models.IntegerField(default = 0)
    fourthname = models.CharField(max_length=30)
    fifthclass = models.IntegerField(default = 0)
    fifthname = models.CharField(max_length=30)
"""
