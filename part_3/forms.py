from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError

# ADDING DATA
class AddPostTherapy(ModelForm):
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }

class EditPostTherapy(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        
        salivary_gland = cleaned_data.get('salivary_gland')
        kidney_left = cleaned_data.get('kidney_left')
        kidney_right = cleaned_data.get('kidney_right')
        if salivary_gland is not None and salivary_gland < 0:
            self.add_error('salivary_gland', 'Salivary Gland dose cannot be negative.')
        if kidney_left is not None and kidney_left < 0:
            self.add_error('kidney_left', 'Left Kidney dose cannot be negative.')
        if kidney_right is not None and kidney_right < 0:
            self.add_error('kidney_right', 'Right Kidney dose cannot be negative.')

        return cleaned_data
    
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }
