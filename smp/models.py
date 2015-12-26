from django.db import models
# Create your models here.
        
class Auther(models.Model):
    name = models.CharField(max_length= 30)
    institution = models.CharField(max_length= 30)
    
class Jounery(models.Model):
    J_name=models.CharField(max_length =30)


class Paper(models.Model):
    auther =  models.ManyToManyField(Auther)
    jounery = models.ManyToManyField(Jounery)
    timestamp = models.DateTimeField(auto_now_add=True)
    pdf = models.FileField(upload_to = './upload/')
    pdfname = models.CharField(max_length = 30)
        

    
    