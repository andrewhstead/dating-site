from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from home.forms import NewTicketForm, TicketMessageForm
from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from home.models import SupportTicket, SupportMessage

# Create your views here.


# The default home page for the site.
def staff_home(request):
    page_name = "Administration Home"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    all_tickets = SupportTicket.objects.filter(agent=user, is_active=True).order_by('-last_message')
    active_tickets = all_tickets.count()

    high_priority = SupportTicket.objects.filter(agent=user, is_active=True, priority="High")\
        .order_by('-last_message')
    medium_priority = SupportTicket.objects.filter(agent=user, is_active=True, priority="Medium")\
        .order_by('-last_message')
    low_priority = SupportTicket.objects.filter(agent=user, is_active=True, priority="Low")\
        .order_by('-last_message')

    args = {
        'active_tickets': active_tickets,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
        'page_name': page_name,
    }

    return render(request, "staff_home.html", args)
