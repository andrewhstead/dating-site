from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User

# Create your views here.


# The main search page.
@login_required(login_url='/login/')
def search_home(request):
    page_name = "Search Home"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    if request.method == 'POST':

        form = SearchForm(request.POST)

        if 'save_yes' in request.POST:
            form.save()

        return redirect(reverse('search_results'))

    else:
        form = SearchForm()

        args = {
            'form': form,
            'button1_text': 'Search and Save',
            'button2_text': 'Search Without Saving',
            'page_name': page_name,
        }

        args.update(csrf(request))
        return render(request, 'search_home.html', args)


# The search results page.
@login_required(login_url='/login/')
def search_results(request):
    page_name = "Search Results"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, 'search_results.html')
