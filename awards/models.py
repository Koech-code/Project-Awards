from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from pyuploadcare.dj.models import ImageField
 
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture=models.ImageField(upload_to='images', default='no picture', null=True, blank=True)
    name=models.CharField(max_length=30)
    bio=models.TextField(max_length=500)

class Projects(models.Model):
    title=models.CharField(max_length=60)
    image=ImageField(manual_crop='1280x720')
    description=models.TextField(max_length=500)
    link=models.URLField(max_length=255)
    date=models.DateField(auto_now_add=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
