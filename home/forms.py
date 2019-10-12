from django import forms
from .models import SupportTicket, SupportMessage


# Form to create a new support ticket.
class NewTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['category', 'priority']


# Form to edit an existing support ticket.
class EditTicketForm(forms.ModelForm):
    class Meta:
        model = SupportTicket
        fields = ['category', 'priority', 'is_active']
        labels = {
            'is_active': 'Active',
        }


# Form to create a message within a support ticket.
class TicketMessageForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['content', 'image']
        labels = {
            'content': 'Message',
            'image': 'Image (optional)',
        }
