from django import forms
from .models import Team, Player

class UploadFileForm(forms.Form):
    file = forms.FileField()

class TeamCreationForm(forms.ModelForm):  # Make sure this is defined as TeamCreationForm
    class Meta:
        model = Team
        fields = ['name', 'leagues']

class AssignPlayerForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.all(), label="Select Player")
