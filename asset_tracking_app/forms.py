from django import forms
from .models import AssetLog

class AssetLogForm(forms.ModelForm):
    class Meta:
        model = AssetLog
        fields = '__all__'
        widgets = {
            
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'checkout_date': forms.TextInput(attrs={'class': 'form-control'}),
            'return_date': forms.TextInput(attrs={'class': 'form-control'}),
            'condition_on_checkout': forms.TextInput(attrs={'class': 'form-control'}),
            'condition_on_return': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        
