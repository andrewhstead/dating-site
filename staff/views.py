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

    active_tickets = SupportTicket.objects.filter(agent=user, status="Active").order_by('-last_updated')
    active_count = active_tickets.count()
    reply_tickets = SupportTicket.objects.filter(agent=user, status="Awaiting Reply").order_by('-last_updated')

    high_priority = active_tickets.filter(priority="High")
    medium_priority = active_tickets.filter(priority="Medium")
    low_priority = active_tickets.filter(priority="Low")

    args = {
        'active_count': active_count,
        'high_priority': high_priority,
        'medium_priority': medium_priority,
        'low_priority': low_priority,
        'reply_tickets': reply_tickets,
        'page_name': page_name,
    }

    return render(request, "staff_home.html", args)
