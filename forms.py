from django import forms
from stories.models import stories
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateForm(forms.ModelForm):

    '''title = forms.CharField(
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
        widget=forms.Textarea(),
    )
    author = forms.CharField(
        max_length=100,
        widget=forms.HiddenInput()
    )'''

    class Meta:
        model = stories
        fields = ('title','description','picture','content',)

class SearchForm(forms.ModelForm):

    search = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'style': 'max-width: 10em'}),
        required=True,
    )

class SignUpForm(UserCreationForm):

    email = forms.EmailField(label="Email Address")

    class Meta:

        model = User
        fields = ("email","username","password1","password2")

