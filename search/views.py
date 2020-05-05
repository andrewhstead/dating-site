from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .forms import SearchForm
from django.shortcuts import render, redirect
from django.urls import reverse
from users.models import User, Gender
from django.http import JsonResponse, HttpResponseRedirect
from .models import Search

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

        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search = search_form.save(False)
            search.user = user
            search.save()
            search_form.save_m2m()

            if 'save_no' in request.POST:
                request.session['save'] = "No"

            return redirect(reverse('search_results', args=(search.pk,)))

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
def search_results(request, search_id):
    page_name = "Search Results"

    user = request.user
    search = Search.objects.get(pk=search_id)

    gender = search.gender.all()

    results = User.objects.filter(gender__in=gender)

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    if request.session['save'] == "No":
        save = "No"
    else:
        save = "Yes"

    args = {
        'page_name': page_name,
        'results': results,
        'search': search,
        'save': save,
    }

    return render(request, 'search_results.html', args)
