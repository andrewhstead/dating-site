from django.contrib import admin
from .models import MessageThread, Message, Interaction

# Register your models here.
admin.site.register(MessageThread)
admin.site.register(Message)
admin.site.register(Interaction)
