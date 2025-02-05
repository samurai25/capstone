from django.test import Client, TestCase
from .models import User, Profile, Project


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
        self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe', bio='I am a software engineer', phone_number='1234567890', github='johndoe', frontend=True, backend=True, database=True, profile_picture='johndoe.jpg')
    
    
    def test_profile(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.first_name, 'John')
        
        
class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
        self.project = Project.objects.create(user=self.user, title='My Project', description='This is my project', frontend=True, backend=True, database=True, github='johndoe/myproject', link_to_live_demo='https://github.com/johndoe/myproject', image='myproject.jpg')
        
    def test_project(self):
        project = Project.objects.get(user=self.user)
        self.assertEqual(project.title, 'My Project')
            

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='johndoe', password='password123', email='johndoe@email.com')
        self.profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe', bio='I am a software engineer', phone_number='1234567890', github='johndoe', profile_picture='johndoe.jpg')
        self.project = Project.objects.create(user=self.user, title='My Project', description='This is my project', frontend=True, backend=True, database=True, github='johndoe/myproject', link_to_live_demo='https://github.com/johndoe/myproject', image='myproject.jpg')
        
        self.client.force_login(self.user)
    
    
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_profile_view(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        
    def test_projects_view(self):
        response = self.client.get('/projects/johndoe/')
        self.assertEqual(response.status_code, 200)
        
    def test_project_view(self):
        response = self.client.get('/project/1/')
        self.assertEqual(response.status_code, 200)
        
    def test_about_view(self):
        response = self.client.get('/about/johndoe/')
        self.assertEqual(response.status_code, 200)
        
    def test_contact_view(self):
        response = self.client.get('/contact/johndoe/')
        self.assertEqual(response.status_code, 200)
        
        
    def test_edit_profile_view(self):
        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        
    def test_add_project_view(self):
        response = self.client.get('/add_project/')
        self.assertEqual(response.status_code, 200)
        
    def test_edit_project_view(self):
        response = self.client.get('/edit_project/1/')
        self.assertEqual(response.status_code, 200)
        
        

