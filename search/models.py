from django.db import models
from world.models import Country, State
from users.models import User, Ethnicity, Hair, Eyes, Gender, Denomination, Relationship, \
    MaritalStatus, Diet, Drinks, Smokes, HasChildren, WantsChildren


# Create your models here.
# Model to store search queries.
class Search(models.Model):
    user = models.ForeignKey(User, related_name='searcher', on_delete=models.CASCADE)
    last_active = models.CharField(max_length=25, blank=True, null=True)
    age_low = models.IntegerField(blank=True, null=True)
    age_high = models.IntegerField(blank=True, null=True)
    profile_picture = models.BooleanField(default=False)
    intro = models.TextField(max_length=100, blank=True, null=True)

    country = models.ManyToManyField(Country, related_name='search', blank=True)
    state = models.ManyToManyField(State, related_name='search', blank=True)
    ethnicity = models.ManyToManyField(Ethnicity, related_name='search', blank=True)
    hair = models.ManyToManyField(Hair, related_name='search', blank=True)
    eyes = models.ManyToManyField(Eyes, related_name='search', blank=True)
    gender = models.ManyToManyField(Gender, related_name='search_gender', blank=True)
    denomination = models.ManyToManyField(Denomination, related_name='search', blank=True)
    looking_for = models.ManyToManyField(Gender, related_name='seeking_gender', blank=True)
    relationship = models.ManyToManyField(Relationship, related_name='search', blank=True)
    marital_status = models.ManyToManyField(MaritalStatus, related_name='search', blank=True)
    diet = models.ManyToManyField(Diet, related_name='search', blank=True)
    drinks = models.ManyToManyField(Drinks, related_name='search', blank=True)
    smokes = models.ManyToManyField(Smokes, related_name='search', blank=True)
    has_children = models.ManyToManyField(HasChildren, related_name='search', blank=True)
    wants_children = models.ManyToManyField(WantsChildren, related_name='search', blank=True)

    key_words = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.user
