from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Search
from django.forms.widgets import TextInput


# Form to make a new search.
class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ['last_active', 'age_low', 'age_high', 'country', 'denomination', 'ethnicity',
                  'hair', 'eyes', 'looking_for', 'gender', 'marital_status', 'profile_picture', 'diet',
                  'drinks', 'smokes', 'gender', 'has_children', 'wants_children', 'key_words']
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