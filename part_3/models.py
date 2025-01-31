from django.db import models
from part_1.models import Patient
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
class PostTherapy(models.Model):
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver')
    )
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pt_patient')
    date_of_post_therapy = models.DateField()
    post_therapy_scan_hours = models.IntegerField(blank=True, null=True)
    with_spect_ct = models.BooleanField()
    lesions = models.CharField(max_length=120, blank=True)
    bone_lesion_details = models.TextField(blank=True, null=True)
    lesion_image = models.ImageField(upload_to="images/", null=True)
    
    #Dosimetry
    salivary_gland = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    kidney_left = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    kidney_right = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    dosimetry_image = models.ImageField(upload_to="images/")
    

    def clean(self):
        if self.salivary_gland is not None and self.salivary_gland < 0:
            raise ValidationError({'salivary_gland': 'Salivary Gland must be non-negative.'})
        if self.kidney_left is not None and self.kidney_left < 0:
            raise ValidationError({'kidney_left': 'Left Kidney must be non-negative.'})
        if self.kidney_right is not None and self.kidney_right < 0:
            raise ValidationError({'kidney_right': 'Right Kidney must be non-negative.'})
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)