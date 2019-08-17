from django.shortcuts import render, get_object_or_404
from .models import MessageThread, Message
from users.models import User
from django.template.context_processors import csrf
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect


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
            # allocate it to the user and the recipient and increment the message count.
            thread = MessageThread(person_1=person_1, person_2=person_2)
            thread.in_thread += 1
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
            # Before saving the message, find the correct thread and increment the message count.
            thread.in_thread += 1
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

            all_messages = thread.messages.all().order_by('created_date')

            for message in all_messages:
                if not message.is_read and user == message.recipient:
                    message.is_read = True
                    message.read_date = datetime.now()
                    message.save()
                    user.new_messages -= 1
                    user.save()

            args = {
                'user': user,
                'thread': thread,
                'form': message_form,
                'all_messages': all_messages,
                'page_name': page_name,
                'other_person': other_person,
                'person_1': person_1.pk,
                'person_2': person_2.pk,
                'button_text': 'Send Message'
            }

            messages.success(request, "Your message was sent!")
            return render(request, 'message_thread.html', args)

    else:

        message_form = MessageForm()

        all_messages = thread.messages.all().order_by('created_date')

        for message in all_messages:
            if not message.is_read and user == message.recipient:
                message.is_read = True
                message.read_date = datetime.now()
                message.save()
                user.new_messages -= 1
                user.save()

        args = {
            'user': user,
            'form': message_form,
            'thread': thread,
            'all_messages': all_messages,
            'page_name': page_name,
            'other_person': other_person,
            'person_1': person_1.pk,
            'person_2': person_2.pk,
            'button_text': 'Send Message'
        }

        return render(request, 'message_thread.html', args)
