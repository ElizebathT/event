# Generated by Django 4.2.4 on 2023-09-28 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0021_attendee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendee',
            name='address',
        ),
    ]
