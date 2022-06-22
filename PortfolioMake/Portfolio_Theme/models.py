from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Theme (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    color1 = models.CharField(max_length=15)
    color2 = models.CharField(max_length=15)
    color3 = models.CharField(max_length=15)

    def __str__(self):
      return(self.user.username+ " " + self.color1)