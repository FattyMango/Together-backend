# Generated by Django 4.1.7 on 2023-02-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_alter_request_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='Volunteer',
            new_name='volunteer',
        ),
    ]
