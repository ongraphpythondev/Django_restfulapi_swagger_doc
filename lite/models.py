from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.TextField(default='no name')
    age = models.IntegerField(default=0)
    gender = models.CharField(default='N/A',max_length=6)
    signature = models.CharField(default='N/A',max_length=10)

class Reader(models.Model):
    name = models.TextField(default='no name')
    age = models.IntegerField(default=0)
    gender = models.CharField(default='N/A',max_length=6)