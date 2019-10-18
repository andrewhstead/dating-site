from django.shortcuts import render
from django.utils import timezone

# Create your views here.


# The home page for the forum.
def forum_home(request):
    page_name = "Discussion Forum"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    return render(request, "forum_home.html", {
        'page_name': page_name
    })
