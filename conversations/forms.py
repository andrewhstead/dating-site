from django import forms
from .models import Message


# Form to create a new message.
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {
            'content': 'Message',
        }
