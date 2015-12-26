from django.db import models
from django.contrib.auth.models import User

class Learn(models.Model):
	User = models.ForeignKey(User)
	Institution = models.CharField(max_length = 100)
	Content = models.CharField(max_length = 100)
	Start_date = models.DateField()
	End_date = models.DateField()