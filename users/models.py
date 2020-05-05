from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from world.models import Country, State
from datetime import date
from django.shortcuts import get_object_or_404


# A function to calculate a user's age from their date of birth.
def user_age(user):
    today = date.today()
    profile = get_object_or_404(User, pk=user.id)
    dob = profile.date_of_birth

    if dob:
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    else:
        age = "-"

    return age


# Create your models here.
# Model to select the user's ethnicity.
class Ethnicity(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's hair colour.
class Hair(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's eye colour.
class Eyes(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's gender.
class Gender(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's denomination.
class Denomination(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's relationship status.
class Relationship(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's marital status.
class MaritalStatus(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's diet.
class Diet(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's drinking habits.
class Drinks(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select the user's smoking habits.
class Smokes(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Model to select whether the user has children.
class HasChildren(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


# Model to select whether the user wants children.
class WantsChildren(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


# Additional fields are added to the AbstractUser model.
class User(AbstractUser):

    objects = UserManager()
    last_active = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    stripe_id = models.CharField(max_length=40, default='', blank=True, null=True)
    subscription_ends = models.DateTimeField(blank=True, null=True)
    subscription_renews = models.BooleanField(default=False)
    subscription_plan = models.CharField(max_length=25, blank=True, null=True)

    profile_picture = models.ImageField(upload_to="images/users", blank=True, null=True)
    intro = models.TextField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)

    ethnicity = models.ForeignKey(Ethnicity, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    hair = models.ForeignKey(Hair, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    eyes = models.ForeignKey(Eyes, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.ForeignKey(Gender, related_name='user_gender', on_delete=models.SET_NULL, blank=True, null=True)
    denomination = models.ForeignKey(Denomination, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    looking_for = models.ForeignKey(Gender, related_name='sought_gender', on_delete=models.SET_NULL, blank=True, null=True)
    relationship = models.ForeignKey(Relationship, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    marital_status = models.ForeignKey(MaritalStatus, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    diet = models.ForeignKey(Diet, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    drinks = models.ForeignKey(Drinks, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    smokes = models.ForeignKey(Smokes, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    has_children = models.ForeignKey(HasChildren, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)
    wants_children = models.ForeignKey(WantsChildren, related_name='users', on_delete=models.SET_NULL, blank=True, null=True)

    new_messages = models.IntegerField(default=0)
    total_messages = models.IntegerField(default=0)
    new_waves = models.IntegerField(default=0)
    total_waves = models.IntegerField(default=0)
    new_favourited = models.IntegerField(default=0)
    total_favourited = models.IntegerField(default=0)
    new_views = models.IntegerField(default=0)
    total_views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.username
