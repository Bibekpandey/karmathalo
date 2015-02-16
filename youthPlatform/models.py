from django.db import models

# Create your models here.

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
