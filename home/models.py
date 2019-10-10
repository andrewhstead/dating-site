from django.db import models
from users.models import User

# Options for type of support ticket.
CATEGORIES = (
    ('Report Harassment', "Report Harassment"),
    ('Report Spam', "Report Spam"),
    ('Account Query', "Account Query"),
    ('Technical Query', "Technical Query"),
)

# Options for support ticket urgency.
PRIORITY = (
    ('Low', "Low"),
    ('Medium', "Medium"),
    ('High', "High"),
)

# Create your models here.


# Support ticket model.
class SupportTicket(models.Model):
    creator = models.ForeignKey(User, related_name='tickets_started', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name='tickets_owned', on_delete=models.CASCADE, default=1)
    category = models.CharField(max_length=25, choices=CATEGORIES, blank=True, null=True)
    priority = models.CharField(max_length=25, choices=PRIORITY, default="Medium", blank=True, null=True)
    started = models.DateTimeField(auto_now_add=True)
    in_thread = models.IntegerField(default=0)
    last_message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.creator, self.started


# Messages within a support ticket.
class SupportMessage(models.Model):
    ticket = models.ForeignKey(SupportTicket, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='message_sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='recipient', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/support", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    read_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.sender, self.recipient, self.created_date
