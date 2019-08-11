from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import RegistrationForm, LoginForm, EditProfileForm, DeletionForm, ChangePasswordForm
from .models import User

# Create your views here.


# Register a new user.
def register(request):
    page_name = "Register an Account"

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
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


# Log a user in to the site.
def login(request):
    page_name = "Log In To Your Account"

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect(request.GET.get('next') or reverse('home'))
            else:
                messages.error(request, "Your username or password was not recognised. Please try again.")

    else:
        form = LoginForm()

    args = {'form': form,
            'page_name': page_name,
            }

    args.update(csrf(request))
    return render(request, 'login.html', args)


# Log a user out from the site.
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out.')

    return redirect(reverse('login'))


# Logged in users can view and edit their own profile.
@login_required(login_url='/login/')
def user_profile(request):
    page_name = "Edit Your Profile"

    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect(reverse('user_profile'))
        else:
            messages.error(request, 'Sorry, we were unable to update your details. Please try again.')

    else:
        form = EditProfileForm(instance=user)

    args = {
        'form': form,
        'button_text': 'Update Profile',
        'page_name': page_name,
    }
    args.update(csrf(request))
    return render(request, 'user_profile.html', args)


# Logged in users can also delete their own profile.
@login_required(login_url='/login/')
def delete_account(request):
    page_name = "Delete Your Account"

    user = request.user

    if request.method == 'POST':
        form = DeletionForm(request.POST)
        if form.is_valid():
            user_to_delete = auth.authenticate(username=user.username,
                                               password=request.POST.get('password'))
            if user_to_delete is not None:
                user_to_delete.delete()
                messages.success(request, 'Your profile has been deleted.')
                return redirect(reverse('login'))
            else:
                messages.error(request, 'Your password was not recognised. Please try again.')

    else:
        form = DeletionForm()

    args = {
        'form': form,
        'button_text': 'Delete Account',
        'page_name': page_name,
    }
    args.update(csrf(request))
    return render(request, 'delete_account.html', args)


# Once logged in, a user can change their password.
@login_required(login_url='/login/')
def change_password(request):
    page_name = "Change Your Password"

    user = request.user

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():
            user_to_change = auth.authenticate(username=user.username,
                                               password=request.POST.get('password'))

            if user_to_change is not None:
                user.set_password(request.POST.get('password1'))
                user.save()
                auth.login(request, user)
                messages.success(request, 'Your password has been changed.')
                return redirect(reverse('user_profile'))

            else:
                messages.error(request, 'Sorry, we were unable to change your password. Please try again.')

    else:
        form = ChangePasswordForm()

    args = {
        'form': form,
        'button_text': 'Change Password',
        'page_name': page_name,
    }
    args.update(csrf(request))
    return render(request, 'change_password.html', args)