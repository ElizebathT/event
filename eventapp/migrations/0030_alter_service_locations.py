# Generated by Django 4.2.4 on 2024-01-17 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0029_location_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='locations',
            field=models.ManyToManyField(related_name='Service', to='eventapp.location'),
        ),
    ]
