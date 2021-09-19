from django.contrib.auth.decorators import login_required
from awards.models import Projects
from .forms import ProjectForm, ProfileForm, RateForm
from django.shortcuts import render
from django.http  import HttpResponse, request
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Profile, Ratings
from .serializer import ProjectSerializer, ProfileSerializer

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    if request.method=='POST':
        form=ProjectForm(request.POST)
        form=ProfileForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
    else:
        form=ProjectForm()
        form=ProfileForm()
    
    try:
        profiles=Profile.objects.all()
        projects=Projects.objects.all()
        # projects = projects[::-1]
        # randoms = random.randint(0, len(projects)-1)
        # random_project = projects[randoms]
        # print(random_project.image)
    except:
        Projects.DoesNotExist,
        profiles.DoesNotExist,
        
        projects = None
        profiles = None

    return render(request, 'index.html', {'projects':projects, 'profiles':profiles, 'form':form })
    
class ProjList(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method=='POST':
        
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
    else:
        form=ProfileForm()
    
    try:
        profiles=Profile.objects.all()
        # projects = projects[::-1]
        # randoms = random.randint(0, len(projects)-1)
        # random_project = projects[randoms]
        # print(random_project.image)
    except Profile.DoesNotExist:
        profiles = None

    return render(request, 'profile.html', {'profiles':profiles, 'form':form })

class ProfList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

@login_required(login_url='/accounts/login/')
def rates(request, project):
    project=Projects.objects.get(title=project)
    rate=Ratings.objects.filter(user=request.user, project=project).first()
    status=None
    if rate is None:
        return status==False
    else:
        return status==True
   
    if request.method=='POST':
        form=RateForm()
        if form.is_valid():
            rating=form.save(commit=False)
            rating.user=request.user
            rate.project=project

            project_ratings=Ratings.objects.filter(project=project)

            design_ratings=[r.design for r in project_ratings]
            design_average=sum(design_ratings) /len(design_ratings)

            

    return render(request, 'modal.html')