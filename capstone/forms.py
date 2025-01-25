from django import forms
from .models import Profile, Project, Certificate


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'role', 'bio', 'frontend', 'backend', 'database', 'phone_number', 'linkedin', 'github', 'country', 'profile_picture']
  

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/certificate',
            }),
        }
          
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'frontend', 'backend', 'database', 'github', 'link_to_live_demo', 'image']    
        
        