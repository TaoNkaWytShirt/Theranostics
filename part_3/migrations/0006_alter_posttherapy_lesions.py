# Generated by Django 4.2.3 on 2023-08-27 09:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('part_3', '0005_alter_posttherapy_dosimetry_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttherapy',
            name='lesions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Prostate', 'Prostate'), ('Lymph Nodes', 'Lymph Nodes'), ('Bones', 'Bones'), ('Lungs', 'Lungs'), ('Liver', 'Liver')], max_length=120),
        ),
    ]