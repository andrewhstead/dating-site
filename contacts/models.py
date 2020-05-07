from __future__ import unicode_literals
from django.db import models
from users.models import User


# Create your models here.
# An overarching model to log all communication between two users.
class Interaction(models.Model):
    person_1 = models.ForeignKey(User, related_name='interaction_1', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(User, related_name='interaction_2', on_delete=models.CASCADE)
    thread_exists = models.BooleanField(default=False)
    thread_started = models.DateTimeField(blank=True, null=True)
    message_count = models.IntegerField(default=0)
    last_message = models.DateTimeField(blank=True, null=True)
    p1_messages = models.IntegerField(default=0)
    p1_last_message = models.DateTimeField(blank=True, null=True)
    p2_messages = models.IntegerField(default=0)
    p2_last_message = models.DateTimeField(blank=True, null=True)
    p1_unread = models.IntegerField(default=0)
    p2_unread = models.IntegerField(default=0)
    p1_waves = models.IntegerField(default=0)
    p2_waves = models.IntegerField(default=0)
    p1_initial_wave = models.DateTimeField(blank=True, null=True)
    p2_initial_wave = models.DateTimeField(blank=True, null=True)
    p1_latest_wave = models.DateTimeField(blank=True, null=True)
    p2_latest_wave = models.DateTimeField(blank=True, null=True)
    p1_favourited = models.BooleanField(default=False)
    p1_favourited_date = models.DateTimeField(blank=True, null=True)
    p2_favourited = models.BooleanField(default=False)
    p2_favourited_date = models.DateTimeField(blank=True, null=True)
    mutual_favourites = models.BooleanField(default=False)
    mutual_date = models.DateTimeField(blank=True, null=True)
    p1_views = models.IntegerField(default=0)
    p1_latest_view = models.DateTimeField(blank=True, null=True)
    p2_views = models.IntegerField(default=0)
    p2_latest_view = models.DateTimeField(blank=True, null=True)
    list_view = models.DateTimeField(blank=True, null=True)
    blocked = models.BooleanField(default=False)
    p1_has_blocked = models.BooleanField(default=False)
    p2_has_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.person_1) + ', ' + str(self.person_2)


# Message thread model for conversations between users.
class MessageThread(models.Model):
    objects = models.Manager()
    person_1 = models.ForeignKey(User, related_name='threads_started', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(User, related_name='threads_received', on_delete=models.CASCADE)
    started = models.DateTimeField(auto_now_add=True)
    in_thread = models.IntegerField(default=0)
    last_message = models.DateTimeField(auto_now_add=True)
    p1_unread = models.IntegerField(default=0)
    p2_unread = models.IntegerField(default=0)

    def __str__(self):
        return self.person_1, self.person_2


# An individual message, attributed to a user an allocated to the relevant thread.
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='messages_sent', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='messages_received', on_delete=models.CASCADE)
    thread = models.ForeignKey(MessageThread, related_name='messages', on_delete=models.CASCADE)
    interaction = models.ForeignKey(Interaction, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    read_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.sender) + " > " + str(self.recipient) + "; " + \
               str(self.created_date.year) + "-" + str(self.created_date.month) + "-" + str(self.created_date.day)


# An wave, attributed to a user and to a recipient.
class Wave(models.Model):
    sender = models.ForeignKey(User, related_name='waves_sent', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='waves_received', on_delete=models.CASCADE)
    initial_date = models.DateTimeField(auto_now_add=True)
    latest_date = models.DateTimeField(auto_now_add=True)
    total_waves = models.IntegerField(default=0)

    def __str__(self):
        return self.sender, self.recipient, self.latest_date


# A link between users where one has added the other as a favourite.
class Favourite(models.Model):
    creator = models.ForeignKey(User, related_name='added_favourite', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='favourited_by', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    is_mutual = models.BooleanField(default=False)
    mutual_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.creator, self.recipient, self.created_date


# A link between users where one has added the other as a favourite.
class ProfileView(models.Model):
    viewer = models.ForeignKey(User, related_name='viewer', on_delete=models.CASCADE)
    viewed = models.ForeignKey(User, related_name='viewed', on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    latest_view = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.viewer, self.viewed, self.latest_view
