from django.contrib import admin
# from django.conf import settings
from . import models

admin.site.register(models.User)
admin.site.register(models.Project)
admin.site.register(models.Skill)
