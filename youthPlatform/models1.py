from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import AbstractBaseUser

# our general person model
class Person(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=30)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname

# the use account model
class Account(Person):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    accountType = models.CharField(max_length = 30)
    institution = models.CharField(max_length = 50)

"""
class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length = 30, null =False, unique=True)
    firstname = models.CharField(max_length = 30, default="")
    lastname = models.CharField(max_length = 30, default="")
    address = models.CharField(max_length = 50, default="")
    contact = models.CharField(max_length = 30, default="")
    email = models.EmailField('email address', unique = True, null=False, default="")
    joined = models.DateTimeField(auto_now_add = True, default=timezone.now)
    is_active = models.BooleanField(default = True)

# account type is integer field -> 1,2,3
    acountType = models.IntegerField(default=0, null=False)
    institution = models.CharField(max_length = 50, default = "", null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
"""

class Qualification(models.Model):
    level = models.CharField(max_length = 20)
    field = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.level+'('+self.field+')'


class Advertisement(models.Model):
    institutionName = models.CharField(max_length = 50)
    institutionDistrict = models.CharField(max_length = 20)
    institutionLocation = models.CharField(max_length = 30)
    institutionContact = models.CharField(max_length = 30)
    institutionWebsite = models.CharField(max_length = 50, blank = True)
    institutionEmail = models.CharField(max_length = 40)
    qualification = models.ManyToManyField(Qualification)
    detail = models.TextField()
    priority = models.IntegerField(default = 3)
    startDate = models.DateField(default = datetime.date.today)
    endDate = models.DateField()

    def was_published_recently(self):
        return self.startDate >= timezone.Now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.institutionName

class TrainingAd(Advertisement):
    duration = models.CharField(max_length = 40)
    cost = models.IntegerField()
    givesJob = models.BooleanField(default = False)

class JobAd(Advertisement):
    skill = models.CharField(max_length = 100)
    salary = models.IntegerField()
    post = models.CharField(max_length = 50)
    givesTraining = models.BooleanField(default = False)


class Idea(Person):
    title = models.CharField(max_length = 150, default="title")
    tags = models.CharField(max_length = 150, default="")
    isAnonymous = models.BooleanField(default = False)
    description = models.TextField()

    def __str__(self):
        return self.title
