from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    about = models.TextField(null = False)
    
    def __str__(self) -> str:
        return self.username
    
class Profile(models.Model):
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    
    IMAGE_MAX_SIZE = (300, 300)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # save the resized image to the file system
        # this is not the model save method!
        image.save(self.image.path)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
    
    def __str__(self) -> str:
        return self.user.username
    
    
class Project(models.Model):
    
    name = models.CharField(max_length = 30, unique = True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'project_images')
    link = models.URLField(null=True, blank=True)
    github = models.URLField(null=True)
    level = models.CharField(max_length = 10, choices = (("basic", "B"), ("destaque", "D")))
    techs = models.CharField(max_length = 300)
    types = models.CharField(max_length = 10, choices = (("front-end", "Front"), ("fullstack", "Full")))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    # published_date = models.DateTimeField(auto_now_add=True)
    # last_updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        # ordering = ['-published_date']
        
    IMAGE_MAX_SIZE = (300, 300)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # save the resized image to the file system
        # this is not the model save method!
        image.save(self.image.path)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()
        
        
class Skill(models.Model):
    Types_choice = (
        ("Front-end", "F"), ("Back-end", "B"),
        ("Desktop", "D"), ("AI/ML", "ML"),
        ("UI/UX", "U"), ("other", "O"),
        )
    name = models.CharField(max_length = 30, unique = True)
    types = models.CharField(max_length = 10, choices = Types_choice)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'