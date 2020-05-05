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
    state = models.ManyToManyField(State, related_name='search')
    ethnicity = models.ManyToManyField(Ethnicity, related_name='search')
    hair = models.ManyToManyField(Hair, related_name='search')
    eyes = models.ManyToManyField(Eyes, related_name='search')
    gender = models.ManyToManyField(Gender, related_name='search_gender')
    denomination = models.ManyToManyField(Denomination, related_name='search')
    looking_for = models.ManyToManyField(Gender, related_name='seeking_gender')
    relationship = models.ManyToManyField(Relationship, related_name='search')
    marital_status = models.ManyToManyField(MaritalStatus, related_name='search')
    diet = models.ManyToManyField(Diet, related_name='search')
    drinks = models.ManyToManyField(Drinks, related_name='search')
    smokes = models.ManyToManyField(Smokes, related_name='search')
    has_children = models.ManyToManyField(HasChildren, related_name='search')
    wants_children = models.ManyToManyField(WantsChildren, related_name='search')

    key_words = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.user
