from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
	name = models.CharField(max_length = 30)

class Cop(models.Model):
	catagory = models.BooleanField()
	owner = models.ForeignKey(User)
	member = models.ManyToManyField(People)
	p_num = models.IntegerField(default = 0)
	start_date = models.DateField()
	end_date = models.DateField()
	place = models.CharField(max_length = 50)
	purpose = models.IntegerField()
	report_name = models.CharField(max_length = 50)
	report_url = models.URLField()
	save_report = models.BooleanField()
	save_photo = models.BooleanField()