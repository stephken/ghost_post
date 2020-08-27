from django import forms
from ghostpost_app.models import Roast_Boast

ROAST_BOAST=((True, "Boast"), (False, "Roast"))

class add_post(forms.ModelForm):
    class Meta:
        model = Roast_Boast
        fields= ['user_input', 'boast']
    