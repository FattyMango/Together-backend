# Generated by Django 4.1.7 on 2023-05-26 10:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
	dependencies = [
		('user', '0006_alter_baseuser_is_active'),
		('report', '0002_report_is_resolved'),
	]

	operations = [
		migrations.AddField(
			model_name='report',
			name='rating',
			field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(5),
			                                                 django.core.validators.MinValueValidator(0)]),
		),
		migrations.AlterField(
			model_name='report',
			name='content',
			field=models.CharField(blank=True, max_length=1000, null=True),
		),
		migrations.AlterField(
			model_name='report',
			name='user',
			field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_user',
			                        to='user.specialneed'),
		),
	]
