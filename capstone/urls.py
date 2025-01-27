
from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

app_name = "capstone"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/<str:username>/", views.about, name="about"),
    path("projects/<str:username>/", views.projects, name="projects"),
    path("contact/<str:username>/", views.contact, name="contact"),
    path("profile/", views.profile, name="profile"),
    path("projects_fetch/", views.projects_fetch, name="projects_fetch"),
    path("delete_project/", views.delete_project, name="delete_project"),
    path("fetch_profile/", views.fetch_profile, name="fetch_profile"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:project_id>/', views.edit_project, name='edit_project'),
    path('project/<int:project_id>/', views.project, name='project'),
]

