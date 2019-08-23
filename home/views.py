from django.shortcuts import render

# Create your views here.


# The default home page for the site.
def home_page(request):
    page_name = "Home Page"

    return render(request, "home.html", {
        'page_name': page_name
    })


# The contact page for the site.
def contact(request):
    page_name = "Contact Us"

    return render(request, "contact.html", {
        'page_name': page_name
    })


# Page to submit or view support tickets.
def support(request):
    page_name = "Support"

    return render(request, "support.html", {
        'page_name': page_name
    })
