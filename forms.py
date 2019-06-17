from django import forms
from stories.models import stories
class CreateForm(forms.ModelForm):
    title = forms.CharField(
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

    class Meta:
        model = stories
        fields = ('title','description','content')
