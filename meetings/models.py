from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from visitors.models import Visitor


class MeetingRoom(models.Model):
    name = models.CharField(max_length=64)
    size = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)

    def __str__(self):
        return self.content


class Meeting(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    visitors = models.ManyToManyField(Visitor)
    meeting_room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.note


departments = (
    (1, 'Production'),
    (2, 'Warehouse'),
    (3, 'M&R'),
    (4, 'QA'),
    (5, 'Supply Chain'),
    (6, 'Purchasing'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.IntegerField(choices=departments)