from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    leagues = models.ManyToManyField(League, blank=True)
    players = models.ManyToManyField('Player', related_name='teams', blank=True)  # Add related_name here

    def __str__(self):
        return self.name

class Player(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    bye_week = models.IntegerField()

    def __str__(self):
        return self.name

class Auction(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Auction for {self.player.name} in {self.league.name}"