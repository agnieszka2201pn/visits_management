import datetime

import pytest
from django.contrib.auth.models import User

from visitors.models import Company, Visitor, Comment
from meetings.models import Organizer, Meeting, MeetingRoom

@pytest.mark.django_db
def test_meeting_add_view(client):
    url = '/add_meeting/'
    user = User.objects.create(username='user1')
    organizer = Organizer.objects.create(user=user, department=3)
    date = datetime.date.today()
    meeting_room = MeetingRoom.objects.create(name='room1', size = 12)
    company = Company.objects.create(name='company1', company_type=3)
    visitors = Visitor.objects.create(first_name='visitor_name', surname='visitor_surname', contact_details='visitor_surname@blabla.com', company=company)
    response = client.post(url, {'organizer': organizer.pk, 'date' : date, 'visitors': visitors.pk, 'meeting_room' : meeting_room.pk, 'note' : 'fake meeting'})
    assert response.status_code == 302
    assert Meeting.objects.count() == 1


@pytest.mark.django_db
def test_meetings_list_view(meetings, client):
    url = '/meetings_list/'
    response = client.get(url)
    assert response.status_code == 200
    list_view = list(response.context['meetings'].values_list('pk', flat=True))
    list_db = list(Meeting.objects.all().values_list('pk', flat=True))
    assert list_view == list_db