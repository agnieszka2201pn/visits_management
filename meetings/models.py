from django.contrib.auth.models import User
from django.db import models
from visitors.models import Visitor, Company


class MeetingRoom(models.Model):
    name = models.CharField(max_length=64)
    size = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


departments = (
    (1, 'Production'),
    (2, 'Warehouse'),
    (3, 'M&R'),
    (4, 'QA'),
    (5, 'Supply Chain'),
    (6, 'Purchasing'),
)
class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.IntegerField(choices=departments)

    def __str__(self):
        return f'{self.user.username} - {self.get_department_display()}'


class Meeting(models.Model):
    organizer = models.ForeignKey(Organizer, on_delete=models.PROTECT)
    date = models.DateField()
    visitors = models.ManyToManyField(Visitor)
    meeting_room = models.ManyToManyField(MeetingRoom)
    note = models.TextField()

    def __str__(self):
        return self.note
