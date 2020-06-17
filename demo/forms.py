from django import forms
from .models import Details

class DetailForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('name', 'text', 'mobile')