
from djongo import models

class User(models.Model):
	_id = models.ObjectIdField()
	username = models.CharField(max_length=150, unique=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	date_joined = models.DateTimeField(auto_now_add=True)
	team = models.CharField(max_length=100, blank=True)
	def __str__(self):
		return self.username

class Team(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100, unique=True)
	members = models.JSONField(default=list)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name

class Activity(models.Model):
	_id = models.ObjectIdField()
	user = models.CharField(max_length=150)
	activity_type = models.CharField(max_length=100)
	duration = models.IntegerField()  # in minutes
	calories_burned = models.FloatField()
	date = models.DateField()
	def __str__(self):
		return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
	_id = models.ObjectIdField()
	team = models.CharField(max_length=100)
	points = models.IntegerField(default=0)
	week = models.CharField(max_length=20)
	def __str__(self):
		return f"{self.team} - {self.week}"

class Workout(models.Model):
	_id = models.ObjectIdField()
	name = models.CharField(max_length=100)
	description = models.TextField()
	difficulty = models.CharField(max_length=50)
	suggested_for = models.JSONField(default=list)
	def __str__(self):
		return self.name
