from datetime import datetime

import pytest
from django.test import Client

import meetings
from visitors.models import Company, Visitor, Comment
from meetings.models import Organizer

@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def visitors():
    company1 = Company.objects.create(name='company1', company_type=1)
    company2 = Company.objects.create(name='company2', company_type=2)
    visitor1 = Visitor.objects.create(first_name='name1',
                                      surname='surname1',
                                      contact_details='name1@gmail.com',
                                      company = company1,
                                      last_training_date=datetime.today().strftime('%Y-%m-%d'))
    visitor2 = Visitor.objects.create(first_name='name2',
                                      surname='surname2',
                                      contact_details='name2@gmail.com',
                                      company = company1,
                                      last_training_date=datetime.today().strftime('%Y-%m-%d'))
    visitor3 = Visitor.objects.create(first_name='name3',
                                      surname='surname3',
                                      contact_details='name3@gmail.com',
                                      company=company2,
                                      last_training_date=datetime.today().strftime('%Y-%m-%d'))
    visitors = [visitor1, visitor2, visitor3]
    return visitors

