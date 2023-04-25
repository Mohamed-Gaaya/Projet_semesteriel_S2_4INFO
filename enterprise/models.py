import cvbuilder.models as cvmodels
from django.conf import settings
from django.db import models
category_choices=[('IT','IT'),('mechanique','mechanique')]
class company(models.Model):
    nom=models.CharField(unique=True,max_length=100)
    logo=models.ImageField()
    category=models.TextField(choices=category_choices)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone=models.CharField(max_length=100)