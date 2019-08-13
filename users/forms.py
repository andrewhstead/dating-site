from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import User
from django.forms.widgets import TextInput
from .widgets import ThumbnailWidget


# Form to register a new user.
class RegistrationForm(UserCreationForm):
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
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['country'].required = True

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


# Simple username and password login.
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# Form for a user to edit their profile. Password field is not needed and so can be excluded.
class EditProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'country',
                  'profile_picture', 'intro', 'text']
        exclude = ['password']
        help_texts = {
            'username': None,
            'email': None,
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
            'intro': 'Introduction (max 100 characters)',
            'text': 'Profile Text (max 1000 characters)',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'date_of_birth': TextInput(attrs={'type': 'date'}),
            'profile_picture': ThumbnailWidget(),
        }


# Form for a user to edit the relationship section of their profile.
class RelationshipForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['gender', 'marital_status', 'looking_for', 'relationship']
        labels = {
            'looking_for': 'Looking For',
            'marital_status': 'Marital Status',
        }


# Form for a user to edit the appearance section of their profile.
class AppearanceForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['ethnicity', 'hair', 'eyes']
        labels = {
            'hair': 'Hair Colour',
            'eyes': 'Eye Colour',
        }


# Form for a user to edit the lifestyle section of their profile.
class LifestyleForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['drinks', 'smokes', 'diet', 'has_children', 'wants_children']
        labels = {
            'has_children': 'Has Children',
            'wants_children': 'Wants Children'
        }


# Form for user to delete their account. Password is required to delete a user's account.
class DeletionForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        return password


# Form for a user to change their password.
# Old password is needed to make a change, new password must then be entered and confirmed.
class ChangePasswordForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Choose New Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['password', 'password1', 'password2']
        labels = {
            'password': 'Current Password',
        }
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            password_error = "Your passwords do not match. Please try again."
            raise ValidationError(password_error)

        return password2
