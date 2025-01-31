# Generated by Django 4.2.5 on 2025-01-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_3', '0009_alter_posttherapy_post_therapy_scan_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttherapy',
            name='dosimetry_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posttherapy',
            name='kidney_left',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posttherapy',
            name='kidney_right',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posttherapy',
            name='lesion_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posttherapy',
            name='salivary_gland',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
