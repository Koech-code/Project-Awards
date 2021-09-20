from django import forms
from django.forms import forms
from pyuploadcare.dj.forms import ImageField
from . models import Profile, Projects, Ratings
from django.forms import ModelForm

class ProjectForm(forms.Form):
    class Meta:
        model=Projects
        fields=('title', 'description', 'date', 'link')

    image=ImageField(label='')


class ProfileForm(forms.Form):
    class Meta:
        model=Profile
        fields=('user', 'name', 'bio')

class RateForm(forms.Form):
    class Meta:
        model=Ratings
        fields=('user','design', 'usability', 'content')

class uploadForm(ModelForm):
   
    class Meta:
        model=Projects
        fields=('title','description', 'link')
