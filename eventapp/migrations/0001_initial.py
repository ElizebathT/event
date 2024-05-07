# Generated by Django 4.2.4 on 2023-09-10 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_organizer', models.BooleanField(default=False)),
                ('is_provider', models.BooleanField(default=False)),
                ('is_attendee', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker_name', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Ms', 'Ms'), ('Mrs', 'Mrs')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('event_type', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], default='offline', max_length=10)),
                ('description', models.TextField()),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('time', models.TimeField()),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('poster', models.URLField(blank=True, null=True)),
                ('organizer_name', models.CharField(max_length=100)),
                ('deadline', models.DateField(blank=True, default=None, null=True)),
                ('fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('livestream', models.URLField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('org_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('speakers', models.ManyToManyField(blank=True, to='eventapp.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('college', models.BooleanField(default=True)),
                ('aicte', models.CharField(blank=True, max_length=255, null=True)),
                ('org_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AICTE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aicte_id', models.CharField(max_length=15, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('departments', models.ManyToManyField(related_name='AICTE', to='eventapp.department')),
                ('programs_offered', models.ManyToManyField(related_name='AICTE', to='eventapp.program')),
            ],
        ),
    ]