from django import forms
from .models import *


class DistanceBasePriceForm(forms.ModelForm):
    class Meta:
        model = DistanceBasePrice
        fields = ['price', 'km_value', 'day', 'is_enabled']  
        labels = {'price': 'Price value', 'is_enabled': 'Enable', 'km_value': 'Enter Km value'}
        widgets = {'price': forms.TextInput(attrs={'class': 'form-control'}), 'km_value': forms.TextInput(attrs={'class': 'form-control'}), 'day': forms.TextInput(attrs={'class': 'form-control'}), 'is_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})}

class DistanceAdditionalPriceForm(forms.ModelForm):
    class Meta:
        model = DistanceAdditionalPrice
        fields = ['price', 'km_value', 'is_enabled']  
        labels = {'price': 'Price value', 'is_enabled': 'Enable', 'km_value': 'Enter Km value'}
        widgets = {'price': forms.TextInput(attrs={'class': 'form-control'}), 'km_value': forms.TextInput(attrs={'class': 'form-control'}), 'is_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})}

class TMFForm(forms.ModelForm):
    class Meta:
        model = TimeMultiplierFactor
        fields = ['price', 'hours', 'is_enabled']  
        labels = {'price': 'Price', 'is_enabled': 'Enable', 'hours': "Hour"}
        widgets = {'price': forms.TextInput(attrs={'class': 'form-control'}),'hours': forms.TextInput(attrs={'class': 'form-control'}),
                   'is_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})}

class WaitingChargeForm(forms.ModelForm):
    class Meta:
        model = WaitingCharge
        fields = ['price', 'per_min', 'is_enabled']  
        labels = {'price': 'Price', 'is_enabled': 'Enable', 'per_min': "Minute"}
        widgets = {'price': forms.TextInput(attrs={'class': 'form-control'}),'per_min': forms.TextInput(attrs={'class': 'form-control'}),
                   'is_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'})}