from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from meetings.models import Organizer

departments = (
    (1, 'Production'),
    (2, 'Warehouse'),
    (3, 'M&R'),
    (4, 'QA'),
    (5, 'Supply Chain'),
    (6, 'Purchasing'),
)

def create_organizers():
    user1 = User.objects.get(pk=1)
    user2 = User.objects.get(pk=2)
    user3 = User.objects.get(pk=3)
    Organizer.objects.create(user=user1, department=4)
    Organizer.objects.create(user=user2, department=6)
    Organizer.objects.create(user=user3, department=1)

class Command(BaseCommand):

    def handle(self, *args, **options):
        create_organizers()
        self.stdout.write(self.style.SUCCESS("models successfully populated"))

