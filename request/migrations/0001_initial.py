# Generated by Django 4.1.7 on 2023-02-27 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=50)),
                ('help_type', models.CharField(choices=[('M', 'Movement'), ('V', 'Visual'), ('E', 'Else')], max_length=1)),
                ('Volunteer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.volunteer')),
                ('specialNeeds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.specialneed')),
            ],
        ),
    ]
