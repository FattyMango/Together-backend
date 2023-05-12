# Generated by Django 4.1.7 on 2023-05-12 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
	dependencies = [
		('request', '0001_initial'),
	]

	operations = [
		migrations.AddField(
			model_name='request',
			name='building',
			field=models.CharField(default='1', max_length=1),
		),
		migrations.AddField(
			model_name='request',
			name='description',
			field=models.TextField(default='no data', max_length=200),
		),
		migrations.AddField(
			model_name='request',
			name='square',
			field=models.CharField(default='A', max_length=2),
		),
	]
