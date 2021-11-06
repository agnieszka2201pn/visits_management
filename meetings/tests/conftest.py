from datetime import datetime
import pytest

from django.contrib.auth.models import User

from visitors.models import Company, Visitor
from meetings.models import Organizer, MeetingRoom, Meeting


@pytest.fixture
def meetings():
    user1 = User.objects.create(username='user1')
    user2 = User.objects.create(username='user2')
    organizer1 = Organizer.objects.create(user=user1, department=1)
    organizer2 = Organizer.objects.create(user=user2, department=2)
    company1 = Company.objects.create(name='company1', company_type=1)
    company2 = Company.objects.create(name='company2', company_type=2)
    visitor1 = Visitor.objects.create(first_name='name1',
                                      surname='surname1',
                                      contact_details='name1@gmail.com',
                                      company=company1)
    visitor2 = Visitor.objects.create(first_name='name2',
                                      surname='surname2',
                                      contact_details='name2@gmail.com',
                                      company=company1)
    visitor3 = Visitor.objects.create(first_name='name3',
                                      surname='surname3',
                                      contact_details='name3@gmail.com',
                                      company=company2)
    meeting_room = MeetingRoom.objects.create(name='room1', size=10)
    note = 'fake meeting note'
    date = datetime.today().strftime('%Y-%m-%d')
    meeting1 = Meeting.objects.create(organizer=organizer1, date=date, meeting_room=meeting_room, note=note)
    meeting1.visitors.set([visitor1, visitor2])
    meeting2 =  Meeting.objects.create(organizer=organizer2, date=date, meeting_room=meeting_room, note=note)
    meeting2.visitors.set([visitor2, visitor3])
    meeting3 = Meeting.objects.create(organizer=organizer1, date=date, meeting_room=meeting_room, note=note)
    meeting3.visitors.set([visitor3, visitor1])
    meetings = [meeting1, meeting2, meeting3]
    return meetings



