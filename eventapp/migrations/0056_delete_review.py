# Generated by Django 4.2.4 on 2024-02-28 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0055_rename_comments_review_comment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
