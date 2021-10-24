# Generated by Django 3.2.8 on 2021-10-24 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='company',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='visitors.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meeting',
            name='note',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Note',
        ),
    ]
