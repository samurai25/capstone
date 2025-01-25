from django.test import Client, TestCase
from .models import User, Profile, Project


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
        self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe', bio='I am a software engineer', phone_number='1234567890',  github='johndoe', frontend=True, backend=True, database=True, profile_picture='johndoe.jpg')
    
    
    def test_profile(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.first_name, 'John')
        
        


