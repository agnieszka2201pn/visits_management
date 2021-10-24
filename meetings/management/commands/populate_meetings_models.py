from django.core.management.base import BaseCommand

from meetings.models import MeetingRoom


def create_meeting_rooms():
    MeetingRoom.objects.create(name='Big Room 1', size=20)
    MeetingRoom.objects.create(name='Big Room 2', size=15)
    MeetingRoom.objects.create(name='Small Room 1', size=5)
    MeetingRoom.objects.create(name='Small Room2', size=8)
    MeetingRoom.objects.create(name= 'Mini room', size=2)


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_meeting_rooms()
        self.stdout.write(self.style.SUCCESS("models successfully populated"))



