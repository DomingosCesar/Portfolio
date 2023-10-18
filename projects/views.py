from django.shortcuts import render
from . import models

def index(request):
    skills = models.Skill.objects.all()
    projects = models.Project.objects.all()
    users = models.User.objects.all()
    us = models.User.objects.get(id = 1)
    return render(request, 'projects/index.html', context = {
        "skills" : skills,
        "projects" : projects,
        "users" : users,
        "us" : us,
    })
    
def project(request):
    projects = models.Project.objects.all()
    return render(request, 'projects/projects.html', context={
        'projects' : projects
    })