from django import forms
from .models import RegistationModel

powerChoices = [
    ('Flight', 'Flight'),
    ('Speed', 'Speed'),
    ('Invisibility','Invisibility'),
    ('Telekenetic','Telekenetic'),
    ('Healing','Healing'),
    ('Other','Other'),
]

class RegistrationForm(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = RegistationModel
        widgets = {
            'richOrPowers': forms.RadioSelect(),
            'powers': forms.CheckboxSelectMultiple(choices=powerChoices),
            'integrity': forms.Select(),
        }

