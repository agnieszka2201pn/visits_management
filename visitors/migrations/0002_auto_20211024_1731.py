# Generated by Django 3.2.8 on 2021-10-24 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.visitor'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors.company'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='last_training_date',
            field=models.DateField(null=True),
        ),
    ]
