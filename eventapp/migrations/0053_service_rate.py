# Generated by Django 4.2.4 on 2024-02-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0052_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='rate',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
