from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


company_types = (
    (1, 'our company'),
    (2, 'supplier'),
    (3, 'customer'),
    (4, 'auditor'),
    (5, 'authorities'),
    (6, 'other'),
)

class Company(models.Model):
    name = models.CharField(max_length=128)
    company_type = models.IntegerField(choices=company_types)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    contact_details = models.TextField(null=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    last_training_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ('surname',)

    def __str__(self):
        return f'{self.surname} {self.first_name}'


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey('meetings.Organizer', on_delete=models.PROTECT)
    visitor = models.ForeignKey(Visitor, on_delete=models.PROTECT)

    def __str__(self):
        return self.content

