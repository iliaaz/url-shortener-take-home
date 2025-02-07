from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(required=True, max_length=255)
    hashed_url = forms.CharField(required=False, max_length=10, empty_value=None)
    input_pin = forms.CharField(required=False, max_length=10, empty_value=None)
