from django.db import migrations, models
import django.core.validators

def convert_platelet_to_int(apps, schema_editor):
    Screening = apps.get_model('part_1', 'Screening')
    for screening in Screening.objects.all():
        if screening.platelet is not None:
            screening.platelet = int(float(screening.platelet))
            screening.save()

class Migration(migrations.Migration):
    dependencies = [
        ('part_4', '0007_alter_followup_platelet'),  # Replace with your actual previous migration
    ]

    operations = [
        migrations.RunPython(convert_platelet_to_int),
        migrations.AlterField(
            model_name='followup',
            name='platelet',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]
