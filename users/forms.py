from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User


# Form to register a new user.
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First Name'
    )
    last_name = forms.CharField(
        label='Last Name'
    )
    password1 = forms.CharField(
        label='Choose a Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        help_texts = {
            'username': None,
            'email': None,
        }
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        kwargs.setdefault('label_suffix', '')
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            password_error = "Your passwords do not match. Please try again."
            raise ValidationError(password_error)

        return password2

    def save(self, commit=True):
        instance = super(RegistrationForm, self).save()

        return instance
