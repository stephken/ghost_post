from django import forms

ROAST_BOAST=((True, "Boast"), (False, "Roast"))

class add_roastboast(forms.Form):
    roastboast = forms.ChoiceField(choices=ROAST_BOAST)
    content = forms.CharField(max_length=200)