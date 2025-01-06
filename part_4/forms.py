from .models import *
from django import forms
from django.forms import ModelChoiceField, ModelForm

# ADDING DATA
class AddFollowUp(ModelForm):
    def clean_psa(self):
        psa = self.cleaned_data.get('psa')
        if psa is not None and psa < 0:
            raise forms.ValidationError("PSA must be a non-negative value.")
        return psa

    def clean_creatinine(self):
        creatinine = self.cleaned_data.get('creatinine')
        if creatinine is not None and creatinine < 0:
            raise forms.ValidationError("Creatinine must be a non-negative value.")
        return creatinine

    def clean_wbc(self):
        wbc = self.cleaned_data.get('wbc')
        if wbc is not None and wbc < 0:
            raise forms.ValidationError("WBC must be a non-negative value.")
        return wbc

    def clean_rbc(self):
        rbc = self.cleaned_data.get('rbc')
        if rbc is not None and rbc < 0:
            raise forms.ValidationError("RBC must be a non-negative value.")
        return rbc

    def clean_hemoglobin(self):
        hemoglobin = self.cleaned_data.get('hemoglobin')
        if hemoglobin is not None and hemoglobin < 0:
            raise forms.ValidationError("Hemoglobin must be a non-negative value.")
        return hemoglobin

    def clean_hematocrit(self):
        hematocrit = self.cleaned_data.get('hematocrit')
        if hematocrit is not None and hematocrit < 0:
            raise forms.ValidationError("Hematocrit must be a non-negative value.")
        return hematocrit

    def clean_platelet(self):
        platelet = self.cleaned_data.get('platelet')
        if platelet is not None and platelet < 0:
            raise forms.ValidationError("Platelet count must be a non-negative value.")
        return platelet

    def clean_lactate_hydrogenase(self):
        lactate_hydrogenase = self.cleaned_data.get('lactate_hydrogenase')
        if lactate_hydrogenase is not None and lactate_hydrogenase < 0:
            raise forms.ValidationError("Lactate Hydrogenase must be a non-negative value.")
        return lactate_hydrogenase

    def clean_alkaline_phosphatase(self):
        alkaline_phosphatase = self.cleaned_data.get('alkaline_phosphatase')
        if alkaline_phosphatase is not None and alkaline_phosphatase < 0:
            raise forms.ValidationError("Alkaline Phosphatase must be a non-negative value.")
        return alkaline_phosphatase

    def clean_sgpt(self):
        sgpt = self.cleaned_data.get('sgpt')
        if sgpt is not None and sgpt < 0:
            raise forms.ValidationError("SGPT must be a non-negative value.")
        return sgpt

    def clean_sgot(self):
        sgot = self.cleaned_data.get('sgot')
        if sgot is not None and sgot < 0:
            raise forms.ValidationError("SGOT must be a non-negative value.")
        return sgot

    def clean_bilirubins(self):
        bilirubins = self.cleaned_data.get('bilirubins')
        if bilirubins is not None and bilirubins < 0:
            raise forms.ValidationError("Bilirubins must be a non-negative value.")
        return bilirubins

    def clean_gapsma_prostate_suv(self):
        suv = self.cleaned_data.get('gapsma_prostate_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    # Add similar clean methods for other SUV fields (lymph node, bone, brain, lung, liver)
    def clean_gapsma_lymph_node_suv(self):
        suv = self.cleaned_data.get('gapsma_lymph_node_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_gapsma_bone_suv(self):
        suv = self.cleaned_data.get('gapsma_bone_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_gapsma_brain_suv(self):
        suv = self.cleaned_data.get('gapsma_brain_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_gapsma_lung_suv(self):
        suv = self.cleaned_data.get('gapsma_lung_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_gapsma_liver_suv(self):
        suv = self.cleaned_data.get('gapsma_liver_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    # Similar clean methods for FDGPETCT SUV fields
    def clean_fdgpetct_prostate_suv(self):
        suv = self.cleaned_data.get('fdgpetct_prostate_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_fdgpetct_lymph_node_suv(self):
        suv = self.cleaned_data.get('fdgpetct_lymph_node_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_fdgpetct_bone_suv(self):
        suv = self.cleaned_data.get('fdgpetct_bone_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_fdgpetct_brain_suv(self):
        suv = self.cleaned_data.get('fdgpetct_brain_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_fdgpetct_lung_suv(self):
        suv = self.cleaned_data.get('fdgpetct_lung_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv

    def clean_fdgpetct_liver_suv(self):
        suv = self.cleaned_data.get('fdgpetct_liver_suv')
        if suv is not None:
            if suv < 0:
                raise forms.ValidationError("SUV must be a non-negative value.")
        return suv
    
    def clean_gapsma_prostate_size(self):
        size = self.cleaned_data.get('gapsma_prostate_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_gapsma_lymph_node_size(self):
        size = self.cleaned_data.get('gapsma_lymph_node_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_gapsma_bone_size(self):
        size = self.cleaned_data.get('gapsma_bone_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_gapsma_brain_size(self):
        size = self.cleaned_data.get('gapsma_brain_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_gapsma_lung_size(self):
        size = self.cleaned_data.get('gapsma_lung_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_gapsma_liver_size(self):
        size = self.cleaned_data.get('gapsma_liver_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_fdgpetct_prostate_size(self):
        size = self.cleaned_data.get('fdgpetct_prostate_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_fdgpetct_lymph_node_size(self):
        size = self.cleaned_data.get('fdgpetct_lymph_node_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_fdgpetct_bone_size(self):
        size = self.cleaned_data.get('fdgpetct_bone_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_fdgpetct_brain_size(self):
        size = self.cleaned_data.get('fdgpetct_brain_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    def clean_fdgpetct_lung_size(self):
        size = self.cleaned_data.get('fdgpetct_lung_size')
        if size is not None:
            if size < 0:
                raise forms.ValidationError("Size must be a non-negative value.")
        return size

    class Meta:
        model = FollowUp
        fields = ['date_of_follow_up', 'psa', 'creatinine', 'wbc', 'rbc', 'hemoglobin', 'hematocrit', 'platelet', 'lactate_hydrogenase', 'alkaline_phosphatase', 'sgpt', 'sgot', 'bilirubins', 
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

        widgets = {
            'date_of_follow_up': forms.DateInput(attrs={'type': 'date'}),
            'psa': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'creatinine': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'wbc': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'rbc': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'hemoglobin': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'hematocrit': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'platelet': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'lactate_hydrogenase': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'alkaline_phosphatase': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'sgpt': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'sgot': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'bilirubins': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            
            # SUV fields with specific validation
            'gapsma_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'gapsma_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'gapsma_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'gapsma_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'gapsma_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'gapsma_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            
            'fdgpetct_prostate_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'fdgpetct_lymph_node_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'fdgpetct_bone_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'fdgpetct_brain_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'fdgpetct_lung_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),
            'fdgpetct_liver_suv': forms.NumberInput(attrs={'min': '0', 'step': '0.1'}),

            # size fields with specific validation
            'gapsma_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'gapsma_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'gapsma_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'gapsma_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'gapsma_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'gapsma_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            
            'fdgpetct_prostate_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'fdgpetct_lymph_node_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'fdgpetct_bone_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'fdgpetct_brain_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'fdgpetct_lung_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
            'fdgpetct_liver_size': forms.NumberInput(attrs={'min': '0', 'step': '1'}),
        }
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

class EditFollowUp(AddFollowUp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta(AddFollowUp.Meta):
        model = FollowUp
        # This will inherit all fields and widgets from AddFollowUp.Meta
        # but specifically set the model to FollowUp for editing existing records