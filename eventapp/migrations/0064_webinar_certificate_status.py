# Generated by Django 4.2.4 on 2024-03-20 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0063_participationcertificate_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='certificate_status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
