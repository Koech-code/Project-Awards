from django import forms
from django.forms import forms
from pyuploadcare.dj.forms import ImageField
from . models import Profile, Projects

class ProjectForm(forms.Form):
    class Meta:
        model=Projects
        fields=('title', 'description', 'date', 'link')

    image=ImageField(label='')


class ProfileForm(forms.Form):
    class Meta:
        model=Profile
        fields=('user', 'name', 'bio')

    profile_picture=ImageField(label='')
