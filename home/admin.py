from django.contrib import admin
from .models import SupportTicket
from .models import SupportMessage

# Register your models here.
admin.site.register(SupportTicket)
admin.site.register(SupportMessage)
