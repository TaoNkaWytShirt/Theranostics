
from django.db import migrations, models

def convert_platelet_to_int(apps, schema_editor):
    Screening = apps.get_model('part_1', 'Screening')
    for screening in Screening.objects.all():
        if screening.platelet is not None:
            screening.platelet = int(float(screening.platelet))
            screening.save()

class Migration(migrations.Migration):
    dependencies = [
        ('part_1', '0021_alter_physicalexam_bp_alter_physicalexam_ecog_score_and_more'),  # Replace with your actual previous migration
    ]

    operations = [
        migrations.RunPython(convert_platelet_to_int),
        migrations.AlterField(
            model_name='screening',
            name='platelet',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
