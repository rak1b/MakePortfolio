
from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
# Create your models here.

class heroModel(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    before_name = models.CharField(max_length=100,null=True,blank=True,default="Hi,my name is..")
    fullname = models.CharField(max_length=100,null=True,blank=True,default="FirstName LastName")
    before_description = models.CharField(max_length=100,null=True,blank=True,default="I create stuff for the Internet.")
    description = models.CharField(max_length=100,null=True,blank=True,default="I am a Fullstack Web Devoloper From Bangladesh.I use React + Django stack.Currently open for work 😀")
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.username + self.description

class projectsModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    short_description = models.CharField(max_length=250)
    full_description = FroalaField()
    image = models.ImageField(upload_to ='projects/')
    created = models.DateTimeField(auto_now_add=True)
