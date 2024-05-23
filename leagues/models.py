from django.db import models
from django.contrib.auth.models import User

class League(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='leagues')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    leagues = models.ManyToManyField(League, related_name='teams')

    def __str__(self):
        return self.name

class Player(models.Model):
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    bye_week = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Auction(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Auction for {self.player.name} in {self.league.name}"
