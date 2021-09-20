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

    def delete_profile(self):
        self.delete()

    
    def save_profile(self):
        self.save()


class Projects(models.Model):
    title=models.CharField(max_length=60)
    image=ImageField(manual_crop='1280x720')
    description=models.TextField(max_length=500)
    link=models.URLField(max_length=255)
    date=models.DateField(auto_now_add=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return f'{self.title}'

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()


class Ratings(models.Model):
    rating=((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),)
    design=models.IntegerField(choices=rating, default=0, blank=True)
    usability=models.IntegerField(choices=rating, blank=True)
    content=models.IntegerField(choices=rating, blank=True)
    design_average=models.FloatField(default=0, blank=True)
    usability_average=models.FloatField(default=0, blank=True)
    content_average=models.FloatField(default=0, blank=True)
    score=models.FloatField(default=0, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project=models.ForeignKey(Projects, on_delete=models.CASCADE, null=True)

    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Ratings.objects.filter(project_id=id).all()
        return ratings(len(ratings) == 1)

    def __str__(self):
        return f'{self.post} Rating'




