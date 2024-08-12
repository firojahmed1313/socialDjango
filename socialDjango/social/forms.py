from django import forms
from .models import Social

class SocialForm(forms.ModelForm):
    class Meta:
        model=Social
        fields=['text', 'image']