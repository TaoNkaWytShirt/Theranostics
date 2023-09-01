# Generated by Django 4.2.3 on 2023-09-01 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0014_alter_screening_patient'),
        ('part_3', '0006_alter_posttherapy_lesions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posttherapy',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pt_patient', to='part_1.patient'),
        ),
    ]
