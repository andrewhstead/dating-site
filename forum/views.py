from django.shortcuts import render
from django.utils import timezone
from .models import Section, Board, Thread, Post
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from .forms import ThreadForm, PostForm

# Create your views here.


# The home page for the forum.
def forum_home(request):
    page_name = "Discussion Forum"

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    sections = Section.objects.all()
    boards = Board.objects.all()

    args = {
        'user': user,
        'page_name': page_name,
        'sections': sections,
        'boards': boards,
    }

    return render(request, "forum_home.html", args)


# The page to display an individual board.
def board_home(request, board_id):

    board = Board.objects.get(pk=board_id)

    threads = Thread.objects.filter(board=board_id)

    page_name = "Forum: " + board.title

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    args = {
        'user': user,
        'page_name': page_name,
        'board': board,
        'threads': threads,
    }

    return render(request, "board.html", args)


# The page to display an individual board.
@login_required(login_url='/login/')
def new_thread(request, board_id):
    board = Board.objects.get(pk=board_id)

    page_name = "New Thread: " + board.title

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            # Before saving the thread, allocate it to the user and to the selected board and increment the post count.
            thread = thread_form.save(False)
            thread.user = request.user
            thread.board = board
            thread.post_count += 1
            thread.save()
            # Increment the thread and post count for the relevant board.
            board.post_count += 1
            board.thread_count += 1
            board.save()

            # Before saving the post, allocate it to the user and to the new thread.
            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.board = board
            post.save()

            messages.success(request, "Your thread was created!")
            return redirect(reverse('board_home', args={board.pk}))

    else:
        thread_form = ThreadForm()
        post_form = PostForm()

    args = {
        'user': user,
        'page_name': page_name,
        'thread_form': thread_form,
        'post_form': post_form,
        'board': board,
        'button_text': 'Start Thread',
    }
    args.update(csrf(request))

    return render(request, "thread_form.html", args)


# The page to display an individual thread.
def view_thread(request, thread_id):

    thread = Thread.objects.get(pk=thread_id)
    posts = thread.posts.all().order_by('created_date')
    board = Board.objects.get(pk=thread.board_id)

    thread.views += 1
    thread.save()

    page_name = "Thread: " + thread.title

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    args = {
        'user': user,
        'page_name': page_name,
        'board': board,
        'thread': thread,
        'posts': posts,
    }

    return render(request, "thread.html", args)


# Add a new post to an existing thread.
@login_required(login_url='/login/')
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            # Don't save the post until it has been allocated to the user and to the relevant thread.
            post = form.save(False)
            post.user = request.user
            post.thread = thread
            post.board = thread.board
            post.save()
            # Update the thread's last_post field with the current time, and increment the post count by one.
            thread.last_post = timezone.now()
            thread.post_count += 1
            thread.save()
            post.board.post_count += 1
            post.board.save()

            messages.success(request, "Your post was successful!")

        return redirect(reverse('view_thread', args={thread.pk}))

    else:
        form = PostForm()

    args = {
        'form': form,
        'thread': thread,
        'button_text': 'Submit Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)