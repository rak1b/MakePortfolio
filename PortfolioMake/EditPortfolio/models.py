from statistics import mode
from django.db import models

# Create your models here.

class heroModel(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    before_name = models.CharField(max_length=100,null=True,blank=True)
    fullname = models.CharField(max_length=100,null=True,blank=True)
    before_description = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=100,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + self.description