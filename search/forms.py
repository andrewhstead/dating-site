from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Search
from django.forms.widgets import TextInput


# Form to make a new search.
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ['last_active', 'age_low', 'age_high', 'country', 'gender', 'looking_for', 'ethnicity',
                  'hair', 'eyes', 'marital_status', 'denomination', 'diet', 'drinks', 'smokes',
                  'has_children', 'wants_children', 'key_words', 'profile_picture']
        exclude = ['password']
        help_texts = {
            'username': None,
            'email': None,
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Show only users with profile picture:',
            'intro': 'Introduction (max 100 characters)',
            'text': 'Profile Text (max 1000 characters)',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'marital_status': forms.CheckboxSelectMultiple,
            'denomination': forms.CheckboxSelectMultiple,
            'gender': forms.CheckboxSelectMultiple,
            'looking_for': forms.CheckboxSelectMultiple,
            'ethnicity': forms.CheckboxSelectMultiple,
            'hair': forms.CheckboxSelectMultiple,
            'eyes': forms.CheckboxSelectMultiple,
            'diet': forms.CheckboxSelectMultiple,
            'drinks': forms.CheckboxSelectMultiple,
            'smokes': forms.CheckboxSelectMultiple,
            'has_children': forms.CheckboxSelectMultiple,
            'wants_children': forms.CheckboxSelectMultiple,
        }