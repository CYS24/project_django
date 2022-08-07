from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=50)
    addr = models.TextField()
    rdate = models.DateTimeField()

class Brd(models.Model):
    writer = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.TextField()
    content = models.TextField()
    wdate = models.DateTimeField()
    
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    pwd = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    rdate = models.DateTimeField()
    udate = models.DateTimeField()
    