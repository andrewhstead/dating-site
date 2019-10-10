from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone

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
def support(request):
    page_name = "Support"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, "support.html", {
        'page_name': page_name
    })


# Page to create a new support ticket.
def new_ticket(request):
    page_name = "New Support Ticket"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, "new_ticket.html", {
        'page_name': page_name
    })
