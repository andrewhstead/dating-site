from django.shortcuts import render

# Create your views here.


# The default home page for the site.
def home_page(request):
    page_name = "Home Page"

    return render(request, "home.html", {
        'page_name': page_name
    })