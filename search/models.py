from django.db import models
from world.models import Country
from users.models import User

# Options for ethnicity of user.
ETHNICITY = (
    ('Black', "Black"),
    ('White', "White"),
    ('Asian', "Asian"),
)

# Options for hair colour of user.
HAIR = (
    ('Black', "Black"),
    ('Brown', "Brown"),
    ('Blonde', "Blonde"),
    ('Red', "Red"),
    ('Grey', "Grey"),
    ('Bald', "Bald"),
    ('Other', "Other"),
)

# Options for eye colour of user.
EYES = (
    ('Brown', "Brown"),
    ('Blue', "Blue"),
    ('Green', "Green"),
    ('Grey', "Grey"),
    ('Other', "Other"),
)

# Options for denomination of user.
DENOMINATION = (
    ('Catholic', "Catholic"),
    ('Anglican', "Anglican"),
    ('Methodist', "Methodist"),
    ('Baptist', "Baptist"),
)

# Options for diet of user.
DIET = (
    ('Meat Eater', "Meat Eater"),
    ('Vegetarian', "Vegetarian"),
    ('Pescatarian', "Pescatarian"),
    ('Vegan', "Vegan"),
    ('Marmite Only', "Marmite Only"),
)

# Options for drinking habits of user.
DRINKS = (
    ('Never', "Never"),
    ('Occasionally', "Occasionally"),
    ('Socially', "Socially"),
    ('Often', "Often"),
)

# Options for smoking habits of user.
SMOKES = (
    ('Never', "Never"),
    ('Occasionally', "Occasionally"),
    ('Often', "Often"),
)

# Options for gender of user and person being sought.
GENDER = (
    ('Male', "Male"),
    ('Female', "Female"),
)

# Options for type of relationship being sought.
RELATIONSHIP = (
    ('Friendship', "Friendship"),
    ('Fellowship', "Fellowship"),
    ('Marriage', "Marriage"),
)

# Options for marital status of user and person being sought.
STATUS = (
    ('Single', "Single"),
    ('Married', "Married"),
    ('Separated', "Separated"),
    ('Divorced', "Divorced"),
    ('Widowed', "Widowed"),
)

# Options for children of user and person being sought.
HAS_CHILDREN = (
    ('Yes, living with me', "Yes, living with me"),
    ('Yes, living elsewhere', "Yes, living elsewhere"),
    ('Yes, but grown-up', "Yes, but grown-up"),
    ('No', "No"),
)

# Options for family plans of user and person being sought.
WANTS_CHILDREN = (
    ('No', "No"),
    ('One or Two', "One or Two"),
    ('Lots', "Lots"),
    ('Undecided', "Undecided"),
)


# Create your models here.
# Model to store search queries.
class Search(models.Model):
    user = models.ForeignKey(User, related_name='searcher', on_delete=models.CASCADE)
    last_active = models.CharField(max_length=25, blank=True, null=True)
    age_low = models.IntegerField(blank=True, null=True)
    age_high = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey(Country, related_name='search', on_delete=models.CASCADE)
    denomination = models.CharField(max_length=25, choices=DENOMINATION, blank=True, null=True)
    ethnicity = models.CharField(max_length=25, choices=ETHNICITY, blank=True, null=True)
    hair = models.CharField(max_length=25, choices=HAIR, blank=True, null=True)
    eyes = models.CharField(max_length=25, choices=EYES, blank=True, null=True)
    gender = models.CharField(max_length=25, choices=GENDER, blank=True, null=True)
    looking_for = models.CharField(max_length=25, choices=GENDER, blank=True, null=True)
    relationship = models.CharField(max_length=25, choices=RELATIONSHIP, blank=True, null=True)
    marital_status = models.CharField(max_length=25, choices=STATUS, blank=True, null=True)
    profile_picture = models.BooleanField(default=False)
    intro = models.TextField(max_length=100, blank=True, null=True)
    diet = models.CharField(max_length=25, choices=DIET, blank=True, null=True)
    drinks = models.CharField(max_length=25, choices=DRINKS, blank=True, null=True)
    smokes = models.CharField(max_length=25, choices=SMOKES, blank=True, null=True)
    has_children = models.CharField(max_length=25, choices=HAS_CHILDREN, blank=True, null=True)
    wants_children = models.CharField(max_length=25, choices=WANTS_CHILDREN, blank=True, null=True)
    key_words = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.user
