from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Account)
admin.site.register(models.Advertisement)
admin.site.register(models.TrainingAd)
admin.site.register(models.Idea)
admin.site.register(models.JobAd)
