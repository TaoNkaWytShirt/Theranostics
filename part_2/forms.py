from .models import *
from django import forms
from django.forms import ModelForm

class AddTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma', 'premedications', 'medications', 'furosemide', 'systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'date_of_psma': 'Date of PSMA',
            'systolic': 'Systolic Blood Pressure (mmHg)',
            'diastolic': 'Diastolic Blood Pressure (mmHg)',
            'hr': 'Heart Rate (bpm)',
            'rr': 'Respiratory Rate (bpm)',
            'saturation': 'Oxygen Saturation (%)',
            'date_therapy': 'Date of Therapy',
        }

    def clean(self):
        cleaned_data = super().clean()

        systolic = cleaned_data.get('systolic')
        diastolic = cleaned_data.get('diastolic')
        hr = cleaned_data.get('hr')
        rr = cleaned_data.get('rr')
        saturation = cleaned_data.get('saturation')

        if systolic is not None and systolic < 0:
            self.add_error('systolic', 'Systolic blood pressure must be a non-negative value.')
        if diastolic is not None and diastolic < 0:
            self.add_error('diastolic', 'Diastolic blood pressure must be a non-negative value.')
        if hr is not None and hr < 0:
            self.add_error('hr', 'Heart rate must be a non-negative value.')
        if rr is not None and rr < 0:
            self.add_error('rr', 'Respiratory rate must be a non-negative value.')
        if saturation is not None and saturation < 0:
            self.add_error('saturation', 'Oxygen saturation must be a non-negative value.')

        return cleaned_data



class EditTherapy(ModelForm):
    class Meta:
        model = Therapy
        fields = ['date_of_psma', 'premedications', 'medications', 'furosemide', 'systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'date_of_psma': 'Date of PSMA',
            'systolic': 'Systolic Blood Pressure (mmHg)',
            'diastolic': 'Diastolic Blood Pressure (mmHg)',
            'hr': 'Heart Rate (bpm)',
            'rr': 'Respiratory Rate (bpm)',
            'saturation': 'Oxygen Saturation (%)'
        }

    def clean(self):
        cleaned_data = super().clean()

        systolic = cleaned_data.get('systolic')
        diastolic = cleaned_data.get('diastolic')
        hr = cleaned_data.get('hr')
        rr = cleaned_data.get('rr')
        saturation = cleaned_data.get('saturation')

        if systolic is not None and systolic < 0:
            self.add_error('systolic', 'Systolic blood Pressure must be a non-negative value.')
        if diastolic is not None and diastolic < 0:
            self.add_error('diastolic', 'Diastolic blood pressure must be a non-negative value.')
        if hr is not None and hr < 0:
            self.add_error('hr', 'Heart rate must be a non-negative value.')
        if rr is not None and rr < 0:
            self.add_error('rr', 'Respiratory rate must be a non-negative value.')
        if saturation is not None and saturation < 0:
            self.add_error('saturation', 'Oxygen saturation must be a non-negative value.')

        return cleaned_data