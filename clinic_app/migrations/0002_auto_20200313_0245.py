# Generated by Django 2.2.4 on 2020-03-12 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='start_time',
        ),
    ]
