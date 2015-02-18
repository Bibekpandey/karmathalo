from django.db import models
from django.utils import timezone
import datetime

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
    accountType = models.IntegerField(default=1)
    institution = models.CharField(max_length = 50)



class Advertisement(models.Model):
    institutionName = models.CharField(max_length = 50)
    description = models.TextField()

    def was_published_recently(self):
        return self.startDate >= timezone.Now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.institutionName

class TrainingAd(Advertisement):
    duration = models.CharField(max_length = 40, default="3 months")
    cost = models.IntegerField(default = 1000)
    givesJob = models.BooleanField(default = False)

class JobAd(Advertisement):
    skill = models.CharField(max_length = 100)
    salary = models.IntegerField()
    post = models.CharField(max_length = 50)
    givesTraining = models.BooleanField(default = False)


class Idea(models.Model):
    account = models.ForeignKey(Account)
    title = models.CharField(max_length = 150, default="title")
    tags = models.CharField(max_length = 150, default="")
    isAnonymous = models.BooleanField(default = False)
    description = models.TextField()

    def __str__(self):
        return self.title
