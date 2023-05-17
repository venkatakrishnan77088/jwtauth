from django.db import models

# Create your models here.

from django.db import models


class Register(models.Model):
    #id = models.CharField(null=True, blank=True, max_length=20)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, choices=[
                              ('male', 'Male'), ('female', 'Female')])
    email = models.EmailField()

    def __str__(self):
        return self.username


class Article(models.Model):
    # models.CharField(max_length=50, blank=True, null=True)
    ids = models.CharField(max_length=50, blank=True, null=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
