from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .forms import NewTicketForm, TicketMessageForm
from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import SupportTicket, SupportMessage

# Create your views here.


# The default home page for the site.
def home_page(request):
    page_name = "Home Page"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, "home.html", {
        'page_name': page_name
    })


# The contact page for the site.
def contact(request):
    page_name = "Contact Us"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, "contact.html", {
        'page_name': page_name
    })


# Page to view support tickets or create a new ticket.
@login_required(login_url='/login/')
def support(request):
    page_name = "Support"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    active_tickets = SupportTicket.objects.filter(creator=user.id, is_active=True).order_by('-last_message')
    closed_tickets = SupportTicket.objects.filter(creator=user.id, is_active=False).order_by('-last_message')

    args = {
        'active_tickets': active_tickets,
        'closed_tickets': closed_tickets,
        'page_name': page_name,
    }

    return render(request, "support.html", args)


# Page to create a new support ticket.
@login_required(login_url='/login/')
def new_ticket(request):
    page_name = "New Support Ticket"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    if request.method == 'POST':
        ticket_form = NewTicketForm(request.POST)
        message_form = TicketMessageForm(request.POST, request.FILES)
        if ticket_form.is_valid() and message_form.is_valid():
            ticket = ticket_form.save(False)
            ticket.creator = user
            ticket.in_thread += 1
            ticket.save()
            message = message_form.save(False)
            message.ticket = ticket
            message.sender = user
            message.recipient = ticket.agent
            message_form.save()
            messages.success(request, 'Your ticket has been created.')
            return redirect(reverse('support'))
        else:
            messages.error(request, 'Sorry, we were unable to create your ticket. Please try again.')

    else:
        ticket_form = NewTicketForm(instance=user)
        message_form = TicketMessageForm(instance=user)

    args = {
        'ticket_form': ticket_form,
        'message_form': TicketMessageForm,
        'button_text': 'Submit Ticket',
        'page_name': page_name,
    }
    args.update(csrf(request))
    return render(request, 'new_ticket.html', args)
