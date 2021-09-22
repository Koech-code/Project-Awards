from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponseRedirect
from awards.models import Projects
from .forms import ProjectForm, ProfileForm, RateForm, uploadForm
from django.shortcuts import redirect, render
from django.http  import HttpResponse, request
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Profile, Ratings
from .serializer import ProjectSerializer, ProfileSerializer
from django.contrib import messages

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
    user=request.user
    if request.method=='POST':
        
        form=ProfileForm(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            profile.save()
    else:
        form=ProfileForm()
        
    
    try:
        profiles=Profile.get_profile(user)
    except Profile.DoesNotExist:
        profiles = None

    return render(request, 'profile.html', {'profiles':profiles, 'form':form })


class ProfList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


@login_required(login_url='login')
def rates(request, project):
    projects=Projects.objects.get(id=project)
    rate=Ratings.objects.filter(project=projects).all()
    # status=None
   
    if request.method=='POST':
        form=RateForm(request.POST)
        if form.is_valid():
            rating=form.save(commit=False)
            rating.user=request.user
            rating.project=projects
            rating.save()

            project_ratings=Ratings.objects.filter(project=project)

            design_ratings=[r.design for r in project_ratings]
            design_average=sum(design_ratings) /len(design_ratings)

            content_ratings=[c.content for c in project_ratings]
            content_average=sum(content_ratings) /len(content_ratings)

            usability_ratings=[u.usability for u in project_ratings]
            usability_average=sum(usability_ratings) /len(usability_ratings)

            score=(design_average + content_average + usability_average)/3

            rating.design_average=round(design_average, 2)
            rating.usability_average=round(usability_average, 2)
            rating.content_average=round(content_average, 2)
            rating.score=round(score, 2)
            rating.save()
            print(rating)

            return HttpResponseRedirect(request.path_info)
    else:
        form=RateForm()
    parameters={
        'project':project,
        'rating_form':form,
        'id':project,
        'rate':rate
        # 'rating_status':status
    }
    return render(request, 'rate.html', parameters )


@login_required(login_url='login')
def upload(request):
    currentUser=request.user
    try:
        profile=Profile.objects.get(user=currentUser)
    except Profile.DoesNotExist:
        raise Http404
    if request.method=='POST':
        form=uploadForm(request.POST, request.FILES)
        if form.is_valid():

            image=form.save()
            image.profile=profile
            image.user=request.user
            image.save()
            messages.add_message(request, messages.ERROR, "Project saved successfully")

            return redirect(upload)
    else:
        form=uploadForm()

    return render(request, 'uploads.html', {'form':form})


@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_articles = Projects.objects.filter(title__contains=search_term)
        users=Projects.objects.all()
        print(users)
        message = f"{search_term}"
        print(searched_articles)
        array=[]
        for searched_articles in searched_articles:
            searched_articles=Projects.objects.get(id=searched_articles.id)
            array.append(searched_articles)
        return render(request, 'search.html',{"message":message,"search": array})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})