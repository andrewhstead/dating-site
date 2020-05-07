from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User, user_age
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
from datetime import date, timedelta
from world.models import State

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

    today = date.today()
    users = User.objects.filter(is_staff=False)

    country = request.GET.get('country', '')
    gender = request.GET.get('gender', '')
    ethnicity = request.GET.get('ethnicity', '')
    age_low = request.GET.get('age_low', '')
    age_high = request.GET.get('age_high', '')

    results = users.filter(country_id=country).order_by('-last_active')

    if gender:
        results = results.filter(gender=gender)
    if ethnicity:
        results = results.filter(ethnicity=ethnicity)
    if age_low:
        latest_date = today - timedelta(days=(int(age_low)*365)+(int(age_low)/4)+1)
        results = results.filter(date_of_birth__lte=latest_date)
    if age_high:
        earliest_date = today - timedelta(days=((int(age_high) + 1)*365)+(int(age_high)/4))
        results = results.filter(date_of_birth__gte=earliest_date)

    for result in results:
        one_minute = result.last_active + timedelta(seconds=60)
        if timezone.now() > one_minute:
            result.is_online = False
        else:
            result.is_online = True

    args = {
        'page_name': page_name,
        'results': results,
    }

    return render(request, 'search_results.html', args)
