from datetime import date
from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from contacts.models import MessageThread, ProfileView, Wave, Favourite, Interaction
from .forms import RegistrationForm, LoginForm, EditProfileForm, DeletionForm, \
    ChangePasswordForm, LifestyleForm, AppearanceForm, RelationshipForm
from .models import User, user_age
from datetime import timedelta
from django.utils import timezone

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


# Logged in users can edit their own profile.
@login_required(login_url='/login/')
def user_profile(request):
    page_name = "Edit Your Profile"

    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        lifestyle = LifestyleForm(request.POST, request.FILES, instance=user)
        appearance = AppearanceForm(request.POST, request.FILES, instance=user)
        relationship = RelationshipForm(request.POST, request.FILES, instance=user)
        if form.is_valid() and lifestyle.is_valid() and appearance.is_valid() and relationship.is_valid():
            form.save()
            lifestyle.save()
            appearance.save()
            relationship.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect(reverse('own_profile'))
        else:
            messages.error(request, 'Sorry, we were unable to update your details. Please try again.')

    else:
        form = EditProfileForm(instance=user)
        lifestyle = LifestyleForm(instance=user)
        appearance = AppearanceForm(instance=user)
        relationship = RelationshipForm(instance=user)

    args = {
        'form': form,
        'lifestyle': lifestyle,
        'appearance': appearance,
        'relationship': relationship,
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


# Logged in users can view the profiles of others.
@login_required(login_url='/login/')
def view_profile(request, user_id):
    profile = get_object_or_404(User, pk=user_id)
    user = request.user

    try:
        interaction = Interaction.objects \
            .get(person_1__in=[user.id, profile.id], person_2__in=[user.id, profile.id])
    except Interaction.DoesNotExist:
        interaction = None

    try:
        favourite = Favourite.objects.get(creator=user.id, recipient=profile.id)
    except Favourite.DoesNotExist:
        favourite = None

    try:
        thread = MessageThread.objects \
            .get(person_1__in=[user.id, profile.id], person_2__in=[user.id, profile.id])
    except MessageThread.DoesNotExist:
        thread = None

    try:
        wave = Wave.objects.get(sender=user.id, recipient=profile.id)
    except Wave.DoesNotExist:
        wave = None

    if wave:
        week_ago = wave.latest_date + timedelta(days=7)
        if timezone.now() > week_ago:
            new_wave = True
        else:
            new_wave = False
    else:
        new_wave = True

    try:
        repeat_view = ProfileView.objects.get(viewer=user, viewed=profile)
    except ProfileView.DoesNotExist:
        repeat_view = None

    if interaction:
        if user.id == interaction.person_1 and interaction.p1_latest_wave:
            week_ago = interaction.p1_latest_wave + timedelta(days=7)
        elif user.id == interaction.person_2 and interaction.p2_latest_wave:
            week_ago = interaction.p2_latest_wave + timedelta(days=7)
        if timezone.now() > week_ago:
            new_wave = True
        else:
            new_wave = False
        if interaction.thread_exists:
            thread_exists = True
            person_1 = interaction.person_1
            person_2 = interaction.person_2
        else:
            thread_exists = False
    else:
        thread_exists = False
        new_wave = True

    if thread:
        thread_exists = True
        person_1 = thread.person_1
        person_2 = thread.person_2
    else:
        thread_exists = False
        person_1 = 0
        person_2 = 0

    # Get the age of the user from their date of birth.
    age = user_age(profile)

    if user.id == profile.id:
        page_name = "Your Profile"
        return redirect('/profile/')
    else:
        page_name = profile.username + "'s Profile"

        # Add one to the profile owner's new views and total views.
        profile.new_views += 1
        profile.total_views += 1
        profile.save()

        # Update the interaction views or create a new interaction.
        if interaction:
            if user.id == interaction.person_1:
                interaction.p1_views += 1
                interaction.p1_latest_view = timezone.now()
                interaction.save()
            else:
                interaction.p2_views += 1
                interaction.p2_latest_view = timezone.now()
                interaction.save()
        else:
            interaction = Interaction(person_1=user, person_2=profile)
            interaction.p1_views += 1
            interaction.p1_latest_view = timezone.now()
            interaction.save()

        # Create a new profile view and allocate it to the user and the profile owner.
        if repeat_view:
            repeat_view.views += 1
            repeat_view.latest_view = timezone.now()
            repeat_view.save()
        else:
            new_view = ProfileView(viewer=user, viewed=profile)
            new_view.views += 1
            new_view.latest_view = timezone.now()
            new_view.save()

    return render(request, 'view_profile.html', {
        'profile': profile,
        'page_name': page_name,
        'thread_exists': thread_exists,
        'new_wave': new_wave,
        'person_1': person_1,
        'person_2': person_2,
        'user': user,
        'age': age,
        'favourite': favourite,
    })


# Logged in users can also view their own profile.
@login_required(login_url='/login/')
def own_profile(request):
    user = request.user
    profile = get_object_or_404(User, pk=user.id)
    page_name = "Your Profile"

    # Get the age of the user from their date of birth.
    age = user_age(user)

    return render(request, 'view_profile.html', {
        'profile': profile,
        'page_name': page_name,
        'user': user,
        'age': age,
    })
