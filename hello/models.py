from django.db import models

# Create your models here.

class Talents(models.Model):
    TalentId= models.AutoField(primary_key=True)
    TalentName=models.CharField(max_length=500)