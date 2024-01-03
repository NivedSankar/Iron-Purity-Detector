from django import forms
from .models import MLModelData

class IronForm(forms.ModelForm):
    class Meta:
        model = MLModelData
        fields = "__all__"
        widgets = {
            'iron_feed': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'silica_feed': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'starch_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'amina_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'ore_pulp_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'ore_pulp_density': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_04_air_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_05_air_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_06_air_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_07_air_flow': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_01_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_02_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_03_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_04_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_05_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_06_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
            'column_07_level': forms.NumberInput(attrs={'class': 'form-control','style': 'width: 300px'}),
        }
              