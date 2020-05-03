from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


# The main search page.
@login_required(login_url='/login/')
def search_home(request):
    page_name = "Search Home"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    args = {
        'page_name': page_name,
    }

    return render(request, "search_home.html", args)
