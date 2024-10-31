from django import forms
from .models import URL

class URLForm(forms.ModelForm):
    original_url = forms.URLField(
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = URL
        fields = ['original_url']