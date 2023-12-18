from django.db import models

# Create your models here.
class MyModel(models.Model):
    username = models.CharField(max_length=100)
    passsword = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    session_token = models.CharField(max_length=100)
class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()