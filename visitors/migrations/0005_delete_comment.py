# Generated by Django 3.2.8 on 2021-10-25 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_alter_visitor_last_training_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
