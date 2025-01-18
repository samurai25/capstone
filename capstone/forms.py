from django import forms
from .models import Profile, Project


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'frontend', 'backend', 'database', 'phone_number', 'github', 'profile_picture']
            
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'frontend', 'backend', 'database', 'github', 'link_to_live_demo', 'image']    
        