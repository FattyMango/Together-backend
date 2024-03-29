# Generated by Django 4.1.7 on 2023-04-02 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('justID', models.PositiveIntegerField(unique=True, verbose_name='university ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='full name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_online', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('user.baseuser',),
        ),
        migrations.CreateModel(
            name='SpecialNeed',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('disability_type', models.CharField(choices=[('M', 'Movement'), ('V', 'Visual'), ('E', 'Else')], max_length=1, verbose_name='type of disability')),
            ],
            options={
                'abstract': False,
            },
            bases=('user.baseuser',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_validated', models.BooleanField(default=False, verbose_name='is the user valid to volunteer')),
            ],
            options={
                'abstract': False,
            },
            bases=('user.baseuser',),
        ),
    ]
