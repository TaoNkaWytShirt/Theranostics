# Generated by Django 4.2.5 on 2025-01-07 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_4', '0009_auto_20250107_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='hemoglobin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='rbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='followup',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
