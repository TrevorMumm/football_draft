from django import forms
from .models import Team, Player

class UploadFileForm(forms.Form):
    file = forms.FileField()

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class AssignPlayerForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.all(), label="Select Player")