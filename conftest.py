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





