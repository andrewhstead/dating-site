from django.contrib import admin
from .models import Section, Board, Thread, Post

# Register your models here.
admin.site.register(Section)
admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Post)
