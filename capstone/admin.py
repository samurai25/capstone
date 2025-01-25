from django.contrib import admin
from .models import User, Profile, Project, Certificate

# Register your models here.
admin.site.register(User)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)

admin.site.register(Project)
admin.site.register(Certificate)

