import datetime

import pytest
from django.contrib.auth.models import User, Permission
from django.test import Client

from visitors.models import Company, Visitor, Comment
from meetings.models import Organizer, Meeting, MeetingRoom

@pytest.mark.django_db
def test_meeting_add_view(client):
    user = User.objects.create(username='user1')
    user.set_password('1234$#@!')
    user.save()
    p = Permission.objects.get(codename='add_meeting')
    user.user_permissions.add(p)
    c=Client()
    url1 = '/login/'
    response_login = c.post(url1, {'username':'user1', 'password':'1234$#@!'})
    assert response_login.status_code == 302
    url2 = '/add_meeting/'
    organizer = Organizer.objects.create(user=user, department=3)
    date = datetime.date.today()
    meeting_room = MeetingRoom.objects.create(name='room1', size = 12)
    company = Company.objects.create(name='company1', company_type=3)
    visitors = Visitor.objects.create(first_name='visitor_name', surname='visitor_surname', contact_details='visitor_surname@blabla.com', company=company)
    response = c.post(url2, {'organizer': organizer.pk, 'date' : date, 'visitors': visitors.pk, 'meeting_room' : meeting_room.pk, 'note' : 'fake meeting'})
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


@pytest.mark.django_db
def test_meeting_delete_view(meetings, client):
    user = User.objects.create(username='test_user')
    user.set_password('1234$#@!')
    user.save()
    p = Permission.objects.get(codename='delete_meeting')
    user.user_permissions.add(p)
    c = Client()
    url1 = '/login/'
    response_login = c.post(url1, {'username': 'test_user', 'password': '1234$#@!'})
    assert response_login.status_code == 302
    count_before = Meeting.objects.count()
    meeting = Meeting.objects.get(pk=1)
    url2 = f'/delete_meeting/{meeting.id}/'
    response = c.delete(url2, {'pk':meeting.id})
    assert response.status_code == 302
    count_after = Meeting.objects.count()
    assert count_before == count_after + 1


@pytest.mark.django_db
def test_organizer_add_view(client):
    url = '/add_organizer/'
    user = User.objects.create(username='new_user')
    response = client.post(url, {'user':user.pk,
                                 'department':1})
    assert response.status_code == 302
    assert Organizer.objects.count() == 1


@pytest.mark.django_db
def test_meeting_update_view(meetings, client):
    user = User.objects.create(username='test_user')
    user.set_password('1234$#@!')
    user.save()
    p = Permission.objects.get(codename='change_meeting')
    user.user_permissions.add(p)
    c = Client()
    url1 = '/login/'
    response_login = c.post(url1, {'username': 'test_user', 'password': '1234$#@!'})
    assert response_login.status_code == 302
    meeting = meetings[0]
    url = f'/update_meeting/{meeting.pk}/'
    response_get = c.get(url)
    meeting_data = response_get.context['form'].initial
    meeting_data['visitors'] = (1,2)
    meeting_data['note'] = 'new note'
    response = c.post(url, meeting_data)
    changed_meeting = Meeting.objects.get(pk=meeting.pk)
    assert changed_meeting.note == 'new note'
    assert response.status_code == 302


@pytest.mark.django_db
def test_meeting_search_view(meetings, client):
    meeting1 = meetings[0]
    organizer1 = meeting1.organizer
    url = f'/search_meeting/'
    response = client.get(url, {'organizer': organizer1.pk})
    assert len(response.context_data['meeting_list']) == len(Meeting.objects.filter(organizer=organizer1.pk))
    assert response.status_code == 200


