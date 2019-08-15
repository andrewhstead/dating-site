from django.db import models
from users.models import User


# Create your models here.
# Message thread model for conversations between users.
class MessageThread(models.Model):
    objects = models.Manager()
    person_1 = models.ForeignKey(User, related_name='threads_started', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(User, related_name='threads_received', on_delete=models.CASCADE)
    started = models.DateTimeField(auto_now_add=True)
    in_thread = models.IntegerField(default=0)
    last_message = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.person_1) + '-' + unicode(self.person_2)


# An individual message, attributed to a user an allocated to the relevant thread.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    thread = models.ForeignKey(MessageThread, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.sender) + " -> " + unicode(self.recipient) + ", " + unicode(self.created_date)
