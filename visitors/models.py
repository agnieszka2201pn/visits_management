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
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    last_training_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.first_name}, {self.surname}, company: {self.company}'


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
