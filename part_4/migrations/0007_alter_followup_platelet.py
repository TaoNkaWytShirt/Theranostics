# Generated by Django 4.2.5 on 2025-01-07 06:03

from django.db import migrations, models
import part_4.models


class Migration(migrations.Migration):

    dependencies = [
        ('part_4', '0006_alter_followup_platelet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='platelet',
            field=models.IntegerField(blank=True, null=True, validators=[part_4.models.FollowUp.validate_platelet_digits]),
        ),
    ]
