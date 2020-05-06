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

    # if request.method == 'POST':
    #
    #     search_form = SearchForm(request.POST)
    #
    #     if search_form.is_valid():
    #         search = search_form.save(False)
    #         search.user = user
    #         search.save()
    #         search_form.save_m2m()
    #
    #         if 'save_no' in request.POST:
    #             request.session['save'] = "No"
    #
    #         return redirect(reverse('search_results', args=(search.pk,)))

    form = SearchForm()

    if form.is_valid():

        gender = request.GET.get('q')
        results = User.objects.filter(Q(gender__icontains=gender))

        args = {
            "gender": gender,
            "results": results,
        }

        return render(request, "search_results.html", args)

    else:
        args = {
            'form': form,
            'submit_text': 'Search',
            # 'button2_text': 'Search Without Saving',
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

    # search = Search.objects.get(pk=search_id)
    # results = User.objects.all()
    # gender = search.gender.all()
    # hair = search.hair.all()
    #
    # if gender:
    #     results = results.filter(Q(gender__in=gender))
    # if hair:
    #     results = results.filter(Q(hair__in=hair))

    # if request.session['save'] == "No":
    #     search.delete()

    args = {
        'page_name': page_name,
        # 'results': results,
        # 'search': search,
    }

    return render(request, 'search_results.html', args)
