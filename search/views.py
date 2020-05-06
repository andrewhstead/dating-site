from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q

# Create your views here.


# The main search page.
@login_required(login_url='/login/')
def search_home(request):
    page_name = "Search Home"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    form = SearchForm()

    args = {
        'form': form,
        'submit_text': 'Search',
        'page_name': page_name,
    }

    return render(request, 'search_home.html', args)


# The search results page.
@login_required(login_url='/login/')
def search_results(request):
    page_name = "Search Results"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    country = request.GET.get('country', '')
    gender = request.GET.get('gender', '')

    results = User.objects.filter(country_id=country)

    if gender:
        results = results.filter(gender=gender)

    args = {
        'page_name': page_name,
        'results': results,
    }

    return render(request, 'search_results.html', args)
