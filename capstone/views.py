from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django import forms
from .models import User, Profile, Project, Certificate
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, ProjectForm, CertificateForm
from django.shortcuts import get_object_or_404
from django.core.cache import cache 



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        
        
def registration_view(request):
    
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})
    
   
def index(request):
    return render(request, 'index.html')


def about(request, username):
    try:
        user = User.objects.get(username=username)
        try:
            profile = Profile.objects.get(pk=user.id)
            certificates = Certificate.objects.filter(user=user)
            certificates_list = list(certificates.values('id', 'url'))
        except:
            profile = None
            certificates_list = []
    except:
        profile = None
        
    return render(request, 'capstone/about.html', {
        'profile': profile,
        'certificates': certificates_list
    })
    
@login_required
def projects(request, username):

    return render(request, 'capstone/projects.html')

def contact(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except:
        profile = None
    return render(request, 'capstone/contact.html', {'profile': profile})

@login_required
def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'capstone/profile.html')
    return render(request, 'capstone/error.html')

@login_required
def projects_fetch(request):
    user = request.user
    if user.is_authenticated:
        projects = cache.get('projects')
        if not projects:
            projects = Project.objects.filter(user=user).all().values().order_by('-created_at')
            cache.set('projects', list(projects), 60)  # Cache for 60 seconds
        else:
            projects = cache.get('projects')
        
    
        return JsonResponse(list(projects), safe=False)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)


@login_required
def delete_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        project_id = data['project_id']
        project = Project.objects.get(id=project_id)
        project.delete()
        
        cache.delete('projects')  # Delete cache when a new project is added or updated
        
        username = request.user.username
        
        return JsonResponse({
            'success': True,
            'message': 'Project deleted successfully',
            'redirect_url': '/projects/{}/'.format(username)
        }, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def edit_project(request, project_id):
    user = request.user
    if user.is_authenticated:
        if project_id:
            projects = Project.objects.filter(user=user)
            project = projects.get(pk=project_id)

            form = ProjectForm(instance=project)
            
            if request.method == 'POST':
                form = ProjectForm(request.POST, request.FILES)
                if form.is_valid():

                    project.title = form.cleaned_data['title']
                    project.description = form.cleaned_data['description']
                    project.frontend = form.cleaned_data['frontend']
                    project.backend = form.cleaned_data['backend']
                    project.database = form.cleaned_data['database']
                    project.github = form.cleaned_data['github']
                    project.link_to_live_demo = form.cleaned_data['link_to_live_demo']
                    
                    if 'image-clear' in request.POST:
                        project.image.delete(save=False)
                        project.image = None 
                    elif 'image' in request.FILES:
                        project.image = form.cleaned_data['image']
                    
                    project.updated_at = timezone.now()
                    project.save()
                    cache.delete('projects')  # Delete cache when a new project is added or updated
                    # redirect back to edit project page
                    return redirect('capstone:project', project_id=project_id)
                    
            else:
                form = ProjectForm(instance=project)
        return render(request, 'capstone/edit_project.html', {'form': form, 'project': project})
    else:
        return render(request, 'capstone/error.html')

@login_required   
def fetch_profile(request):
    user = request.user

    if user.is_authenticated:

        try:
            # Cache the profile data to improve performance and reduce database load
            profile = cache.get('profile')
            if not profile:
                profile = Profile.objects.get(pk=user.id)
                cache.set('profile', profile, 60)  # Cache for 60 seconds
        except:
            profile = Profile.objects.create(user=user)
            profile.save()
            cache.set('profile', profile, 60)  # Cache for 60 seconds
            
        certificates = Certificate.objects.filter(user=user)
        certificates_list = list(certificates.values('id', 'url'))  # Convert QuerySet to list of dictionaries  
          
        data = {
            'id': profile.id,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'role': profile.role,
            'email': user.email,
            'phone_number': profile.phone_number,
            'github': profile.github,
            'linkedin': profile.linkedin,
            'country': profile.country,
            'bio': profile.bio,
            'frontend': profile.frontend,
            'backend': profile.backend,
            'database': profile.database,
            'profile_picture': str(profile.profile_picture),
            'certificates': certificates_list
        }

        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=400)

@login_required   
def edit_profile(request):
    user = request.user

    profile = user.profile 
    certificates = Certificate.objects.filter(user=user)
  
    if user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            
            if 'save_profile' in request.POST and form.is_valid():
                profile = form.save(commit=False)
                profile.first_name = form.cleaned_data['first_name']
                profile.last_name = form.cleaned_data['last_name']
                profile.role = form.cleaned_data['role']
                profile.bio = form.cleaned_data['bio']
                profile.frontend = form.cleaned_data['frontend']
                profile.backend = form.cleaned_data['backend']
                profile.database = form.cleaned_data['database']
                profile.phone_number = form.cleaned_data['phone_number']
                profile.github = form.cleaned_data['github']
                profile.linkedin = form.cleaned_data['linkedin']
                profile.country = form.cleaned_data['country']
                
                if 'image-clear' in request.POST:
                    profile.profile_picture.delete(save=False)
                    profile.profile_picture = None 
                elif 'profile_picture' in request.FILES:
                    profile.profile_picture = form.cleaned_data['profile_picture']
                    
                profile.save()
                cache.delete('profile') # Delete cache when the profile is edited
                return redirect('capstone:profile')
            
            certificate_form = CertificateForm(request.POST)
            if 'add_certificate' in request.POST and certificate_form.is_valid():
                certificate = certificate_form.save(commit=False)
                certificate.user = user
                certificate.url = certificate_form.cleaned_data['url']
                certificate.save()
                
                return redirect('capstone:edit_profile')
            
            if 'delete_certificate' in request.POST:
                certificate_id = request.POST.get('certificate_id')
                Certificate.objects.filter(id=certificate_id, user=user).delete()
                return redirect('capstone:edit_profile')
            
        else:
            form = ProfileForm(instance=profile)
            certificate_form = CertificateForm()
        
        return render(request, 'capstone/edit_profile.html', {
            'form': form,
            'certificate_form': certificate_form,
            'certificates': certificates,
            
            })
    else:
        return render(request, 'capstone/error.html')

@login_required       
def add_project(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = Project.objects.create(user=user, 
                                title=form.cleaned_data['title'], 
                                description=form.cleaned_data['description'], 
                                frontend=form.cleaned_data['frontend'],
                                backend=form.cleaned_data['backend'], 
                                database=form.cleaned_data['database'],
                                github=form.cleaned_data['github'],
                                link_to_live_demo=form.cleaned_data['link_to_live_demo'], 
                                image=form.cleaned_data['image'],
                                created_at=timezone.now()
                            )
                
                project.save()
                cache.delete('projects')  # Delete cache when a new project is added or updated
                return redirect('capstone:projects', username=user.username)
        else:
            form = ProjectForm()
        return render(request, 'capstone/add_project.html', {'form': form})
    else:
        return render(request, 'capstone/error.html')
    
@login_required
def project(request, project_id):
    if project_id:
        project = Project.objects.get(pk=project_id)
        return render(request, 'capstone/project.html', {'project': project})
    else:
        return redirect('capstone:index')
    
    
def error(request):
    return render(request, 'capstone/error.html')