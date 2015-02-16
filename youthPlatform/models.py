from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
'''
class Person(models.Model):
	name = models.CharField()
	address = mdoels..
	contact =  ...
	email = ...

	def __str__(self):
		pass


class Account(Person):
	username = ...
	password = ...
	accountType = ...
	institution = models.Char...

class Qualification(models.Model):
	level = models.CharField()...
	field = models.Charfield().. # can be null

class Advertisement(models.Model):
	institutionName = models.Charfi...
	institutionDistrict = models.Charfield
	institutionLocation = models.charfield...
	institutionContact = mdoels
	institutionWebsite = models...
	institutionEmail = models...
	qualification = models.ManyToManyField(Qualification)
	detail = models.TextField...
	priority = models.IntegerField()
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()

	def wasPublishedRecently(self):
		return ...

class TrainingAd(Advertisement):
	duration = models.Charfield()
	cost = models.IntegerField()
	givesJob = models.BooleanField()

class JobAd(Advertisement):
	skill = models.CharField
	salary = models.IntegerField
	post = models.CharField...
	givesTraining = models.BooleanField()

class Idea(Person):
	isAnonymous = models.BooleanField(default=False)
	description = models.TextField()
'''

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

class Qualification(models.Model):
    level = models.CharField(max_length = 20)
    field = models.CharField(max_length = 20)

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
    isAnonymous = models.BooleanField(default = False)
    description = models.TextField()
