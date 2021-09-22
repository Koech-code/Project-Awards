from django import forms
from . models import Profile, Projects, Ratings


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields=('title', 'description', 'link')

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('name', 'bio')

class RateForm(forms.ModelForm):
    class Meta:
        model=Ratings
        fields=('design', 'usability', 'content')

class uploadForm(forms.ModelForm):
    class Meta:
        model=Projects
        fields=('title', 'image', 'description', 'link')
