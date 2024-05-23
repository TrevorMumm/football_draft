from django import forms
from .models import Team

class UploadFileForm(forms.Form):
    file = forms.FileField()

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'leagues']