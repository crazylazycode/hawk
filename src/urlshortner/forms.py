from django import forms

from .validators import validate_url,validate_dot_com

class SubmitURLForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Shorten Your Link",
                "class": "form-control"
                }
        )
    )