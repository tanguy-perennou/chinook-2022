from django import forms

class SearchForm(forms.Form):
    """
    Simplest possible form, just a text box for a query
    """
    query = forms.CharField(label='Search in album titles', max_length=100, required=False)