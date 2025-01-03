# Generated by Django 4.2.5 on 2025-01-01 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0017_alter_patient_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gleason_score',
            field=models.IntegerField(blank=True, help_text='Enter a value between 6 and 10', null=True, validators=[django.core.validators.MinValueValidator(6, message='Gleason score must be between 6 and 10'), django.core.validators.MaxValueValidator(10, message='Gleason score must be between 6 and 10')]),
        ),
    ]
