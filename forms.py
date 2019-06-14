from django import forms
class CreateForm(forms.Form):
    Title = forms.CharField(
        label="Title",
        max_length=10,
        widget=forms.TextInput(attrs={'style':'max-width: 10em'}),
        required=True
    )
    description = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'style':'max-width: 15em'}),
        required=True
    )
    content = forms.CharField(
        max_length=100000,
        widget=forms.Textarea()
    )

