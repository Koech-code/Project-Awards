from rest_framework import serializers
from .models import Profile, Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('user','title', 'description', 'image', 'link', 'date')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user','name', 'profile_picture', 'bio')