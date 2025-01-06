from django.db import models
from part_1.models import *
from django.core.validators import MinValueValidator

# class Equipment(models.Model):
#     name = models.CharField(max_length=300,null=True)
#     slug = models.SlugField(null=True)
    
#     def __str__(self):
#         return self.name

#CLASS THERAPY ONLY SUPPORTS ONE ENTRY PER PATIENT AS OF NOW. OPTIMIZE LATER    

class Therapy(models.Model):
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='t_patient')
    date_of_psma = models.DateField()
    premedications = models.CharField(max_length=120, null=True, blank=True)
    medications = models.CharField(max_length=120, null=True, blank=True)
    furosemide = models.BooleanField()
    systolic = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    diastolic = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    hr = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    rr = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    saturation = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)])
    date_therapy = models.DateField()
    radiopharm = models.CharField(max_length=120, null=True, blank=True)
    side_effects = models.CharField(max_length=120, blank=True)

    def clean(self):
        if self.systolic is not None and self.systolic < 0:
            raise ValidationError({'systolic': 'Systolic Blood Pressure Cannot Be Negative.'})
        if self.diastolic is not None and self.diastolic < 0:
            raise ValidationError({'diastolic': 'Diastolic Blood Pressure Cannot Be Negative.'})
        if self.hr is not None and self.hr < 0:
            raise ValidationError({'hr': 'Heart Rate Cannot Be Negative.'})
        if self.rr is not None and self.rr < 0:
            raise ValidationError({'rr': 'Respiratory Rate Cannot Be Negative.'})
        if self.saturation is not None and self.saturation < 0:
            raise ValidationError({'saturation': 'Oxygen Saturation Cannot Be Negative.'})
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)