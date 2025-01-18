
from django.db import models
    
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100, default="", blank=True)
    bio = models.TextField(blank=True)
    frontend = models.CharField(max_length=200, default="", blank=True)
    backend = models.CharField(max_length=200, default="", blank=True)
    database = models.CharField(max_length=200, default="", blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    github = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to="images/", 
                                        blank=True, null=True, verbose_name="image")
    
    
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
    link_to_live_demo = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name="image")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
   
