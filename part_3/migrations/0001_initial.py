# Generated by Django 4.0.4 on 2023-02-08 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('part_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTherapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_post_therapy', models.DateField()),
                ('post_therapy_scan', models.IntegerField(blank=True, null=True)),
                ('furosemide', models.BooleanField()),
                ('lesions', models.CharField(choices=[('Prostate', 'Prostate'), ('Lymph Nodes', 'Lymph Nodes'), ('Bones', 'Bones'), ('Lungs', 'Lungs'), ('Liver', 'Liver')], max_length=120)),
                ('bone_lesion_details', models.TextField(blank=True, null=True)),
                ('lesion_image', models.ImageField(blank=True, upload_to='')),
                ('salivary_gland', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('kidney_left', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('kidney_right', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('dosimetry_image', models.ImageField(blank=True, upload_to='')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part_1.patient')),
            ],
        ),
    ]