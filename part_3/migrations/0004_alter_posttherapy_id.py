# Generated by Django 4.2.3 on 2023-08-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_3', '0003_rename_furosemide_posttherapy_with_spect_ct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttherapy',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]