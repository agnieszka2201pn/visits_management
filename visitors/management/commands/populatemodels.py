from django.core.management.base import BaseCommand

from visitors.models import Company


def create_companies():
    Company.objects.create(name='Big Customer', company_type=3)
    Company.objects.create(name='Small Customer', company_type=3)
    Company.objects.create(name='Main Supplier', company_type=2)
    Company.objects.create(name='SQS', company_type=4)
    Company.objects.create(name='Headquarters', company_type=3)
    Company.objects.create(name='SANEPID', company_type=5)


class Command(BaseCommand):

    def handle(self, *args, **options):
        create_companies()
        self.stdout.write(self.style.SUCCESS("models successfully populated"))



