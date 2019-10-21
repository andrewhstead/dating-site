from django.shortcuts import render
from django.utils import timezone
from .models import Section, Board, Thread, Post

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

    page_name = "Forum: " + board.title

    user = request.user

    if user.is_authenticated:
        user.last_active = timezone.now()
        user.save()

    args = {
        'user': user,
        'page_name': page_name,
        'board': board,
    }

    return render(request, "board.html", args)
