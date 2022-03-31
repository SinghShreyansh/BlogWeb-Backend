from django.db import models

# Create your models here.

class Blogs(models.Model):
    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    body=models.CharField(max_length=50000)
    author=models.CharField(max_length=500)
    category=models.CharField(max_length=500)