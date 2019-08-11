from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistrationForm
from .models import User

# Create your views here.


# Register a new user.
def register(request):
    page_name = "Register an Account"

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, label_suffix='')
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                messages.success(request, 'Your registration was successful!')
                auth.login(request, user)
                return redirect(request.GET.get('next') or reverse('home'))
            else:
                messages.error(request, 'Sorry, we were unable to register your account. Please try again.')

    else:
        form = RegistrationForm()

    args = {
        'form': form,
        'button_text': 'Register',
        'page_name': page_name,
    }
    args.update(csrf(request))
    return render(request, 'register.html', args)
