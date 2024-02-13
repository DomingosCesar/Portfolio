from django.shortcuts import render
from . import models

def index(request):
    skills = models.Skill.objects.all()
    projects = models.Project.objects.all()
    profile = models.Profile.objects.all()
    us = models.Profile.objects.get(user = 1)
    print(us.user)
    return render(request, 'projects/index.html', context = {
        "skills" : skills,
        "projects" : projects,
        "profiles" : profile,
        "us" : us,
    })
    
    
def project(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/projects.html', context={
        'projects' : projects
    })