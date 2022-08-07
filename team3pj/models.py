from django.db import models

class User(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    pwd = models.CharField(max_length=128)
    username = models.CharField(max_length=128)    
    rdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.id

class Worldcup(models.Model):
    g_name = models.CharField(max_length=200)
    
class Tables(models.Model):
    subject = models.TextField()
    content = models.TextField()
    name = models.TextField(max_length=128)
    date = models.DateTimeField(auto_now=True)
    views = models.IntegerField()