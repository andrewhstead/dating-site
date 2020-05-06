from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.widgets import TextInput
from users.models import User

# Options for time period when user was last active.
ACTIVE = (
    ('Any Time', "Any Time"),
    ('Today', "Today"),
    ('Last 7 Days', "Last 7 Days"),
    ('Last 14 Days', "Last 14 Days"),
    ('Last Month', "Last Month"),
)


# Form to make a new search.
class SearchForm(forms.ModelForm):

    active = forms.ChoiceField(required=False, choices=ACTIVE, label='Last Active:')
    age_low = forms.IntegerField(required=False, label='Minimum Age')
    age_high = forms.IntegerField(required=False, label='Maximum Age:')
    keywords = forms.CharField(widget=forms.Textarea, required=False)
    picture = forms.BooleanField(required=False, label='Only users with profile picture:')

    class Meta:
        model = User
        fields = ['age_low', 'age_high', 'country', 'gender', 'looking_for', 'ethnicity',
                  'hair', 'eyes', 'marital_status', 'denomination', 'diet', 'drinks', 'smokes',
                  'has_children', 'wants_children', 'keywords', 'picture', 'active']
        exclude = ['password']
        help_texts = {
            'username': None,
            'email': None,
        }
        labels = {
            'country': 'Country (select at least one):'
        }
        widgets = {
            'country': forms.SelectMultiple,
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
