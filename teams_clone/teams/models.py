from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    details = models.TextField()
    department = models.CharField(max_length = 64)
    role = models.CharField(max_length = 16)


class Team(models.Model):
    name = models.CharField(max_length = 64)
    members = models.ManyToManyField(UserProfile, related_name='joined_teams')
    owners = models.ManyToManyField(UserProfile, related_name='owned_teams')

class Channel(models.Model):
    name = models.CharField(max_length = 64)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)

class Message(models.Model):
    date_created = models.DateTimeField()
    content = models.TextField()
    sender = models.OneToOneField(User, on_delete=models.CASCADE)

class PrivateMessage(Message):
    receiver = models.OneToOneField(User, on_delete=models.CASCADE)

class ChannelMessage(Message):
    channel = models.OneToOneField(Channel, on_delete=models.CASCADE)

class GroupMessage(Message):
    receiver = models.OneToOneField(User, on_delete=models.CASCADE)

