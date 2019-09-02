from django.shortcuts import render, get_object_or_404
from .models import MessageThread, ProfileView, Wave, Favourite, Interaction
from users.models import User
from django.template.context_processors import csrf
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.db.models import Q


# Create your views here.
# Create a new conversation, by creating a new message and using it to create the message thread.
@login_required(login_url='/login/')
def new_thread(request, person_1, person_2):

    person_1 = get_object_or_404(User, pk=person_1)
    person_2 = get_object_or_404(User, pk=person_2)

    page_name = "New Message to: " + person_2.username

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # Before saving the message, create the thread,
            # allocate it to the user and the recipient.
            # Increment the message count and unread count.
            thread = MessageThread(person_1=person_1, person_2=person_2)
            thread.in_thread += 1
            thread.p2_unread += 1
            thread.save()

            # Before saving the message, allocate it to the user and the recipient and to the new thread.
            message = message_form.save(False)
            message.sender = person_1
            message.recipient = person_2
            message.thread = thread
            message.save()

            # Add one to the recipient's new message and total message count.
            person_2.new_messages += 1
            person_2.total_messages += 1
            person_2.save()

            messages.success(request, "Your thread was created!")
            return redirect(reverse('message_thread', kwargs={'person_1': person_1.pk, 'person_2': person_2.pk}))

    else:
        message_form = MessageForm()
        args = {
            'page_name': page_name,
            'form': message_form,
            'button_text': 'Send Message',
            'recipient': person_2.username,
        }
        args.update(csrf(request))

        return render(request, 'new_thread.html', args)


# Show the user an individual thread.
def message_thread(request, person_1, person_2):

    user = request.user

    person_1 = get_object_or_404(User, pk=person_1)
    person_2 = get_object_or_404(User, pk=person_2)

    if user == person_1:
        other_person = person_2
    else:
        other_person = person_1

    thread = get_object_or_404(MessageThread, person_1=person_1, person_2=person_2)

    page_name = "Messages: " + other_person.username

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            # Before saving the message, find the correct thread.
            # Increment the total message count and unread count.
            thread.in_thread += 1
            thread.last_message = timezone.now()
            if user == person_1:
                thread.p2_unread += 1
            else:
                thread.p1_unread += 1
            thread.save()

            # Also allocate the message to the user and the recipient and to the thread.
            message = message_form.save(False)
            if user == person_1:
                message.sender = person_1
                message.recipient = person_2
                person_2.new_messages += 1
                person_2.total_messages += 1
                person_2.save()
            else:
                message.sender = person_2
                message.recipient = person_1
                person_1.new_messages += 1
                person_1.total_messages += 1
                person_1.save()
            message.thread = thread
            message.save()

            thread_messages = thread.messages.all().order_by('created_date')

            for message in thread_messages:
                if not message.is_read and user == message.recipient:
                    message.is_read = True
                    message.read_date = timezone.now()
                    message.save()
                    user.new_messages -= 1
                    user.save()
                    if user == person_1:
                        thread.p1_unread -= 1
                        thread.save()
                    else:
                        thread.p2_unread -= 1
                        thread.save()

            args = {
                'user': user,
                'thread': thread,
                'form': message_form,
                'thread_messages': thread_messages,
                'page_name': page_name,
                'other_person': other_person,
                'person_1': person_1.pk,
                'person_2': person_2.pk,
                'button_text': 'Send Message'
            }

            messages.success(request, "Your message was sent!")
            return redirect(reverse('message_thread', kwargs={'person_1': person_1.pk, 'person_2': person_2.pk}))

    else:

        message_form = MessageForm()

        thread_messages = thread.messages.all().order_by('created_date')

        for message in thread_messages:
            if not message.is_read and user == message.recipient:
                message.is_read = True
                message.read_date = timezone.now()
                message.save()
                user.new_messages -= 1
                user.save()
                if user == person_1:
                    thread.p1_unread -= 1
                    thread.save()
                else:
                    thread.p2_unread -= 1
                    thread.save()

        args = {
            'user': user,
            'form': message_form,
            'thread': thread,
            'thread_messages': thread_messages,
            'page_name': page_name,
            'other_person': other_person,
            'person_1': person_1.pk,
            'person_2': person_2.pk,
            'button_text': 'Send Message'
        }

        return render(request, 'message_thread.html', args)


# View a list of all conversations of which the user is a part.
@login_required(login_url='/login/')
def all_messages(request):

    user = request.user

    page_name = "All Messages"

    threads = MessageThread.objects.filter(Q(person_1=user) | Q(person_2=user))\
        .order_by('-last_message')

    args = {
        'page_name': page_name,
        'threads': threads,
    }

    return render(request, 'messages.html', args)


# View a list of other users who have viewed the user's profile.
@login_required(login_url='/login/')
def profile_views(request):

    user = request.user

    if user.new_views > 0:
        user.new_views = 0
        user.save()

    page_name = "Profile Views"

    views = ProfileView.objects.filter(viewed_id=user.id).order_by('-latest_view')

    interactions = Interaction.objects.filter(Q(person_1=user) | Q(person_2=user))

    for interaction in interactions:
        if user.id == interaction.person_1:
            interaction.view_date = interaction.p1_latest_view
        else:
            interaction.view_date = interaction.p2_latest_view

    interactions.order_by('-view_date')

    total_views = user.total_views

    unique_viewers = views.count()

    args = {
        'user': user,
        'page_name': page_name,
        'views': views,
        'interactions': interactions,
        'total_views': total_views,
        'unique_viewers': unique_viewers,
    }

    return render(request, 'profile_views.html', args)


# View a list of other users who have been added as a favourite.
@login_required(login_url='/login/')
def favourites(request):

    user = request.user

    page_name = "Favourites"

    args = {
        'page_name': page_name,
    }

    return render(request, 'favourites.html', args)


# Wave at another user.
@login_required(login_url='/login/')
def waved_at(request, recipient):

    user = request.user
    recipient = get_object_or_404(User, pk=recipient)

    page_name = "Waves Sent"

    try:
        repeat_wave = Wave.objects.get(sender=user, recipient=recipient)
    except Wave.DoesNotExist:
        repeat_wave = None

    # If no previous waves, create a new wave and allocate it to the sender and the recipient.
    # If there are previous waves, update that database record.
    if repeat_wave:
        repeat_wave.total_waves += 1
        repeat_wave.latest_date = timezone.now()
        repeat_wave.save()
    else:
        new_wave = Wave(sender=user, recipient=recipient)
        new_wave.total_waves += 1
        new_wave.initial_date = timezone.now()
        new_wave.latest_date = timezone.now()
        new_wave.save()

    recipient.new_waves += 1
    recipient.total_waves += 1
    recipient.save()

    user_waves = Wave.objects.filter(sender=user).order_by('-latest_date')

    args = {
        'page_name': page_name,
        'user_waves': user_waves,
    }

    messages.success(request, "Your wave was sent!")
    return redirect(reverse('waves_sent'))


# View a list of other users who have waved at the user.
@login_required(login_url='/login/')
def waves(request):

    user = request.user

    page_name = "Waves Sent"

    if user.new_waves > 0:
        user.new_waves = 0
        user.save()

    wave_type = 'received'

    user_waves = Wave.objects.filter(recipient=user).order_by('-latest_date')

    args = {
        'page_name': page_name,
        'user_waves': user_waves,
        'wave_type': wave_type,
    }

    return render(request, 'waves.html', args)


# View a list of other users who have been waved at by the user.
@login_required(login_url='/login/')
def waves_sent(request):

    user = request.user

    page_name = "Waves"

    wave_type = 'sent'

    user_waves = Wave.objects.filter(sender=user).order_by('-latest_date')

    args = {
        'page_name': page_name,
        'user_waves': user_waves,
        'wave_type': wave_type,
    }

    return render(request, 'waves.html', args)


# Add another user to favourites.
@login_required(login_url='/login/')
def favourite_user(request, recipient):

    user = request.user
    recipient = get_object_or_404(User, pk=recipient)

    page_name = "Favourites"

    # Create a new favourite and allocate it to the sender and the recipient.
    new_favourite = Favourite(creator=user, recipient=recipient)
    new_favourite.created_date = timezone.now()
    new_favourite.save()

    recipient.new_favourited += 1
    recipient.total_favourited += 1
    recipient.save()

    try:
        mutual_favourite = Favourite.objects.get(creator=recipient, recipient=user)
    except Favourite.DoesNotExist:
        mutual_favourite = None

    if mutual_favourite:
        mutual_favourite.is_mutual = True
        mutual_favourite.mutual_date = timezone.now()
        mutual_favourite.save()
        new_favourite.is_mutual = True
        new_favourite.mutual_date = timezone.now()
        new_favourite.save()

    user_favourites = Favourite.objects.filter(creator=user).order_by('-created_date')

    args = {
        'page_name': page_name,
        'user_favourites': user_favourites,
    }

    messages.success(request, "User added to favourites.")
    return redirect(reverse('favourites'))


# View a list of other users who the user has added as a favourite.
@login_required(login_url='/login/')
def favourites(request):

    user = request.user

    page_name = "Favourites"

    favourite_type = 'creator'

    favourite_list = Favourite.objects.filter(creator=user).order_by('-created_date')

    args = {
        'page_name': page_name,
        'favourite_list': favourite_list,
        'favourite_type': favourite_type,
    }

    return render(request, 'favourites.html', args)


# View a list of other users who have added the user as a favourite.
@login_required(login_url='/login/')
def favourited_me(request):

    user = request.user

    page_name = "Favourited Me"

    favourite_type = 'recipient'

    favourite_list = Favourite.objects.filter(recipient=user).order_by('-created_date')

    if user.new_favourited > 0:
        user.new_favourited = 0
        user.save()

    args = {
        'page_name': page_name,
        'favourite_list': favourite_list,
        'favourite_type': favourite_type,
    }

    return render(request, 'favourites.html', args)


# View a list of other users who are mutual favourites.
@login_required(login_url='/login/')
def mutual_favourites(request):

    user = request.user

    page_name = "Mutual Favourites"

    favourite_type = 'mutual'

    favourite_list = Favourite.objects.filter(recipient=user, is_mutual=True).order_by('-created_date')

    args = {
        'page_name': page_name,
        'favourite_list': favourite_list,
        'favourite_type': favourite_type,
    }

    return render(request, 'favourites.html', args)
