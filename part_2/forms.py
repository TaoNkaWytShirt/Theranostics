from .models import *
from django import forms
from django.forms import ModelForm

class AddTherapy(ModelForm):
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )

    side_effects = forms.MultipleChoiceField(
        choices=SIDE_EFFECTS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        model = Therapy
        fields = ['date_of_psma', 'premedications', 'medications', 'furosemide', 'systolic', 'diastolic', 'hr', 'rr', 'saturation', 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'systolic': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'diastolic': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'hr': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'rr': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'saturation': forms.NumberInput(attrs={'min': '0', 'max': '100', 'type': 'number'})
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
    SIDE_EFFECTS = (
        ('Fatigue', 'Fatigue'),
        ('Nausea or Vomiting', 'Nausea or Vomiting'),
        ('Dry Lips or Mouth', 'Dry Lips or Mouth'),
        ('Headache', 'Headache'),
        ('Bone Pain', 'Bone Pain')
    )

    side_effects = forms.MultipleChoiceField(
        choices=SIDE_EFFECTS,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # If side_effects is stored as a string
            if isinstance(self.instance.side_effects, str):
                self.initial['side_effects'] = self.instance.side_effects.split(',')
            # If side_effects is already a list
            else:
                self.initial['side_effects'] = self.instance.side_effects

    class Meta:
        model = Therapy
        fields = ['date_of_psma', 'premedications', 'medications', 'furosemide', 
                 'systolic', 'diastolic', 'hr', 'rr', 'saturation', 
                 'date_therapy', 'radiopharm', 'side_effects']
        widgets = {
            'date_of_psma': forms.DateInput(attrs={'type': 'date'}),
            'date_therapy': forms.DateInput(attrs={'type': 'date'}),
            'saturation': forms.NumberInput(attrs={'min': '0', 'max': '100', 'type': 'number'})
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