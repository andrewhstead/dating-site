from django.shortcuts import render, get_object_or_404
from .models import MessageThread, Message
from users.models import User
from django.template.context_processors import csrf
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import MessageForm
from django.contrib import messages


# Create your views here.
# Create a new conversation, by creating a new message and using it to create the message thread.
@login_required(login_url='/login/')
def new_thread(request, person_1, person_2):

    page_name = "Your Profile"

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

            messages.success(request, "Your thread was created!")
            return redirect(reverse('home'))

    else:
        message_form = MessageForm(request.POST)
    args = {
        'page_name': page_name,
        'form': message_form,
        'button_text': 'Send Message',
        'recipient': person_2.username,
    }
    args.update(csrf(request))

    return render(request, 'new_thread.html', args)
