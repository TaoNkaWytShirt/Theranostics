from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from django.core.exceptions import ValidationError

# ADDING DATA
class AddPostTherapy(ModelForm):
    def clean_post_therapy_scan_hours(self):
        hours = self.cleaned_data.get('post_therapy_scan_hours')
        if hours is not None and hours < 0:
            raise forms.ValidationError("Scan hours must be a non-negative value.")
        return hours
    
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver')
    )
    
    lesions = forms.MultipleChoiceField(
        choices=LESIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
            'post_therapy_scan_hours': forms.NumberInput(attrs={
                'min': '0', 
                'type': 'number',
                'class': 'form-control'
            }),
            'salivary_gland': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
            'kidney_left': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
            'kidney_right': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }
        error_messages = {
            'post_therapy_scan_hours': {
                'min_value': 'Scan hours must be a non-negative value.'
            }
        }

class EditPostTherapy(ModelForm):
    LESIONS = (
        ('Prostate', 'Prostate'),
        ('Lymph Nodes', 'Lymph Nodes'),
        ('Bones', 'Bones'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver')
    )
    
    lesions = forms.MultipleChoiceField(
        choices=LESIONS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    def clean_post_therapy_scan_hours(self):
        hours = self.cleaned_data.get('post_therapy_scan_hours')
        if hours is not None and hours < 0:
            raise forms.ValidationError("Scan hours must be a non-negative value.")
        return hours

    def clean(self):
        cleaned_data = super().clean()
        
        # Validate salivary gland value
        salivary_gland = cleaned_data.get('salivary_gland')
        if salivary_gland is not None and salivary_gland < 0:
            self.add_error('salivary_gland', 'Value must be a non-negative value.')

        # Validate kidney values
        kidney_left = cleaned_data.get('kidney_left')
        if kidney_left is not None and kidney_left < 0:
            self.add_error('kidney_left', 'Value must be a non-negative value.')

        kidney_right = cleaned_data.get('kidney_right')
        if kidney_right is not None and kidney_right < 0:
            self.add_error('kidney_right', 'Value must be a non-negative value.')

        return cleaned_data
    
    class Meta:
        model = PostTherapy
        fields = ['date_of_post_therapy','post_therapy_scan_hours','with_spect_ct','lesions','bone_lesion_details', 'lesion_image', 'salivary_gland', 'kidney_left', 'kidney_right', 'dosimetry_image']
        widgets = {
            'date_of_post_therapy': forms.DateInput(attrs={'type': 'date'}),
            'post_therapy_scan_hours': forms.NumberInput(attrs={
                'min': '0', 
                'type': 'number',
                'class': 'form-control'
            }),
            'salivary_gland': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
            'kidney_left': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
            'kidney_right': forms.NumberInput(attrs={
                'min': '0',
                'type': 'number',
                'step': '0.01',
                'class': 'form-control'
            }),
            'lesion_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'dosimetry_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'with_spect_ct': 'With SPECT/CT',
            'post_therapy_scan_hours': 'Therapy Scan Duration (in Hours)'
        }
        error_messages = {
            'post_therapy_scan_hours': {
                'min_value': 'Scan hours must be a non-negative value.'
            }
        }
