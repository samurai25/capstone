
from django.db import models
    
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)


class Profile(models.Model):
    ROLE_CHOICES = (
        ('frontend', 'Frontend Developer'),
        ('backend', 'Backend Developer'),
        ('fullstack', 'Fullstack Developer'),
        ('devops', 'DevOps Engineer'),
        ('qa', 'QA Engineer'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100, default="", blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="frontend")
    bio = models.TextField(blank=True)
    frontend = models.CharField(max_length=200, default="", blank=True)
    backend = models.CharField(max_length=200, default="", blank=True)
    database = models.CharField(max_length=200, default="", blank=True)
    phone_number = models.CharField(max_length=15, default="", blank=True)
    github = models.CharField(max_length=100, default="", blank=True)
    linkedin = models.CharField(max_length=200, default="", blank=True)
    country = models.CharField(max_length=200, default="", blank=True)
    profile_picture = models.ImageField(upload_to="images/", 
                                        blank=True, null=True, 
                                        verbose_name="image")
    
    
    def __str__(self):
        return self.user.username

    

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    frontend = models.CharField(max_length=200, default="", blank=True)
    backend = models.CharField(max_length=200, default="", blank=True)
    database = models.CharField(max_length=200, default="", blank=True)
    github = models.CharField(max_length=200, default="", blank=True)
    link_to_live_demo = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
    url = models.URLField(max_length=500)

    def __str__(self):
        return self.url
    
   
