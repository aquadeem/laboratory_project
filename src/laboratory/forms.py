from django import forms


class IndexForm(forms.Form):
    first_name = forms.CharField(max_length=100)