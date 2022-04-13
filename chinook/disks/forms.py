from django import forms

class SearchForm(forms.Form):
    """
    Simplest possible form, just a text box for a query
    """
    query = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g. all', 'class': 'form-control'}),
        label='Search in album titles', max_length=100, required=False
        )