from django.db import migrations, models
import django.core.validators

def convert_platelet_to_int(apps, schema_editor):
    FollowUp = apps.get_model('part_4', 'FollowUp')
    for follow_up in FollowUp.objects.all():
        if follow_up.platelet is not None:
            follow_up.platelet = int(float(follow_up.platelet))
            follow_up.save()

class Migration(migrations.Migration):
    dependencies = [
        ('part_4', '0008_alter_followup_platelet'),  # Replace with your actual previous migration
    ]

    operations = [
        migrations.RunPython(convert_platelet_to_int),
        migrations.AlterField(
            model_name='followup',
            name='platelet',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999)]),
        ),
    ]
