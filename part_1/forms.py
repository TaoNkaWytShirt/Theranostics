from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field


# ADDING DATA
class AddPatient(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['age'].label = "Age"
        self.fields['address'].label = "Address"
        self.fields['diagnosis_date'].label = "Diagnosis Date"
        self.fields['surgery_date'].label = "Surgery Date"
        self.fields['histopath_result'].label = "Histopathology Result"
        self.fields['histopath_details'].label = "Histopathology Details"
        self.fields['gleason_score'].label = "Gleason Score"
        self.fields['date_of_treatment'].label = "Date of Treatment"
        self.fields['type_of_treatment'].label = "Type of Treatment"
        
        # Add help text for Gleason score
        self.fields['gleason_score'].help_text = "Enter a value between 6 and 10"

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age

    def clean_gleason_score(self):
        score = self.cleaned_data.get('gleason_score')
        if score is not None:
            if score < 6 or score > 10:
                raise forms.ValidationError("Gleason score must be between 6 and 10")
        return score

    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
            'gleason_score': forms.NumberInput(attrs={'min': '6', 'max': '10', 'type': 'number'}),
        }
        error_messages = {
            'name': {'required': "Patient name is required."},
            'age': {'required': "Patient age is required.", 'invalid': "Please enter a valid age."},
            'address': {'required': "Address is required."},
            'diagnosis_date': {'required': "Diagnosis date is required."},
            'surgery_date': {'required': "Surgery date is required."},
            'histopath_result': {'required': "Histopathology result image is required."},
            'histopath_details': {'required': "Histopathology details are required."},
            'gleason_score': {
                'invalid': "Please enter a valid Gleason score (6-10).",
                'min_value': "Gleason score cannot be less than 6.",
                'max_value': "Gleason score cannot be greater than 10."
            },
            'date_of_treatment': {'required': "Treatment date is required."},
            'type_of_treatment': {'required': "Type of treatment is required."}
        }

class EditPatient(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'diagnosis_date', 'surgery_date', 'histopath_result', 'histopath_details', 'gleason_score', 'date_of_treatment', 'type_of_treatment']
        widgets = {
            'diagnosis_date': forms.DateInput(attrs={'type': 'date'}),
            'surgery_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_treatment': forms.DateInput(attrs={'type': 'date'}),
            'age': forms.NumberInput(attrs={'min': '0', 'type': 'number'}),
        }

class PhysicalExamFormBase(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False 
        
        # Add Bootstrap classes to all fields
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
    class Meta:
        model = PhysicalExam
        fields = ['ecog_score', 'height', 'weight', 'bmi', 'bp', 'hr', 'pain_score', 'local_symptoms', 'systemic_symptoms']
        labels = {
            'ecog_score': 'ECOG Performance Status Score',
            'height': 'Height (cm)',
            'weight': 'Weight (kg)',
            'bmi': 'Body Mass Index (BMI)',
            'bp': 'Blood Pressure (mmHg)',
            'hr': 'Heart Rate (bpm)',
            'pain_score': 'Pain Score (0-10)',
            'local_symptoms': 'Local Symptoms',
            'systemic_symptoms': 'Systemic Symptoms'
        }
        widgets = {
            'ecog_score': forms.Select(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'bmi': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'step': '0.01'}),
            'bp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '120/80'}),
            'hr': forms.NumberInput(attrs={'class': 'form-control'}),
            'pain_score': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '10'}),
            'local_symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'systemic_symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }
        help_texts = {
            'bp': 'Systolic/diastolic (e.g., 120/80)',
            'pain_score': '0 (no pain) to 10 (worst pain)',
        }

    def clean_bp(self):
        bp = self.cleaned_data.get('bp')
        if bp:
            # Validate blood pressure format (e.g., "120/80")
            try:
                systolic, diastolic = bp.split('/')
                systolic = int(systolic)
                diastolic = int(diastolic)
            except ValueError:
                raise forms.ValidationError("Blood pressure must be in format 'systolic/diastolic' (e.g. 120/80)")
        return bp

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EditPhysicalExam(PhysicalExamFormBase):
    pass

class AddPhysicalExam(PhysicalExamFormBase):
    pass

class AddScreening(ModelForm):
    class Meta:
        model = Screening
        fields = ['psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
        }

class EditScreening(ModelForm):
    class Meta:
        model = Screening
        fields = ['psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
        'salivary_gland_status', 'salivary_gland_image', 'bone_metastasis_status', 'bone_scan_image', 'renal_scintigraphy', 'gapsma_choices', 'gapsma_img', 
        'gapsma_prostate_lesion_status', 'gapsma_prostate_location', 'gapsma_prostate_suv', 'gapsma_prostate_size',
        'gapsma_lymph_node_lesion_status', 'gapsma_lymph_node_location', 'gapsma_lymph_node_suv', 'gapsma_lymph_node_size',
        'gapsma_bone_lesion_status', 'gapsma_bone_location', 'gapsma_bone_suv', 'gapsma_bone_size',
        'gapsma_brain_lesion_status', 'gapsma_brain_location', 'gapsma_brain_suv', 'gapsma_brain_size',
        'gapsma_lung_lesion_status', 'gapsma_lung_location', 'gapsma_lung_suv', 'gapsma_lung_size',
        'gapsma_liver_lesion_status', 'gapsma_liver_lesion_status', 'gapsma_liver_location', 'gapsma_liver_suv', 'gapsma_liver_size',
        'fdgpetct_img',
        'fdgpetct_prostate_lesion_status', 'fdgpetct_prostate_location', 'fdgpetct_prostate_suv', 'fdgpetct_prostate_size',
        'fdgpetct_lymph_node_lesion_status', 'fdgpetct_lymph_node_location', 'fdgpetct_lymph_node_suv', 'fdgpetct_lymph_node_size',
        'fdgpetct_bone_lesion_status', 'fdgpetct_bone_location', 'fdgpetct_bone_suv', 'fdgpetct_bone_size',
        'fdgpetct_brain_lesion_status', 'fdgpetct_brain_location', 'fdgpetct_brain_suv', 'fdgpetct_brain_size',
        'fdgpetct_lung_lesion_status', 'fdgpetct_lung_location', 'fdgpetct_lung_suv', 'fdgpetct_lung_size',
        'fdgpetct_liver_lesion_status', 'fdgpetct_liver_location', 'fdgpetct_liver_suv', 'fdgpetct_liver_size',
        'assessment', 'plan']
        labels = {
            'psa': 'PSA',
            'creatinine': 'Creatinine(mg/dL)',
            'wbc': 'WBC',
            'rbc' : 'RBC',
            'hemoglobin' : 'Hemogoblin(g/dL)',
            'hematocrit' : 'Hematocrit(%)',
            'platelet' : 'Platelet Count(mcL)',
            'lactate_hydrogenase' : 'Lactate Hydrogenase(units/L)',
            'alkaline_phosphatase' : 'Alkaline Phosphatase(units/L)', 
            'sgpt' : 'SGPT(units/L)', 
            'sgot' : 'SGOT(units/L)', 
            'bilirubins' : 'Bilirubins(mg/dL)',
        }