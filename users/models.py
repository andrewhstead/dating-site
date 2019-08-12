from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from world.models import Country
from datetime import date
from django.shortcuts import get_object_or_404

# Options for ethnicity of user.
ETHNICITY = (
    ('black', "Black"),
    ('white', "White"),
    ('asian', "Asian"),
)

# Options for hair colour of user.
HAIR = (
    ('black', "Black"),
    ('brown', "Brown"),
    ('blonde', "Blonde"),
    ('red', "Red"),
    ('grey', "Grey"),
    ('bald', "Bald"),
    ('other', "Other"),
)

# Options for eye colour of user.
EYES = (
    ('brown', "Brown"),
    ('blue', "Blue"),
    ('green', "Green"),
    ('grey', "Grey"),
    ('other', "Other"),
)

# Options for denomination of user.
DENOMINATION = (
    ('catholic', "Catholic"),
    ('anglican', "Anglican"),
    ('methodist', "Methodist"),
    ('baptist', "Baptist"),
)

# Options for diet of user.
DIET = (
    ('meat-eater', "Meat Eater"),
    ('vegetarian', "Vegetarian"),
    ('pescatarian', "Pescatarian"),
    ('vegan', "Vegan"),
    ('marmite', "Marmite Only"),
)

# Options for gender of user and person being sought.
GENDER = (
    ('M', "Male"),
    ('F', "Female"),
)

# Options for type of relationship being sought.
RELATIONSHIP = (
    ('friendship', "Friendship"),
    ('fellowship', "Fellowship"),
    ('marriage', "Marriage"),
)


# A function to calculate a user's age from their date of birth.
def user_age(user):
    today = date.today()
    profile = get_object_or_404(User, pk=user.id)
    dob = profile.date_of_birth

    if dob:
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    else:
        age = "Not Set"

    return age


# Create your models here.
# Additional fields are added to the AbstractUser model.
class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.ForeignKey(Country, related_name='users', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    stripe_id = models.CharField(max_length=40, default='', blank=True, null=True)
    subscription_ends = models.DateTimeField(blank=True, null=True)
    subscription_renews = models.BooleanField(default=False)
    subscription_plan = models.CharField(max_length=25, blank=True, null=True)
    ethnicity = models.CharField(max_length=25, choices=ETHNICITY, blank=True, null=True)
    hair = models.CharField(max_length=25, choices=HAIR, blank=True, null=True)
    eyes = models.CharField(max_length=25, choices=EYES, blank=True, null=True)
    gender = models.CharField(max_length=25, choices=GENDER, blank=True, null=True)
    looking_for = models.CharField(max_length=25, choices=GENDER, blank=True, null=True)
    relationship = models.CharField(max_length=25, choices=RELATIONSHIP, blank=True, null=True)
    denomination = models.CharField(max_length=25, choices=DENOMINATION, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    diet = models.CharField(max_length=25, choices=DIET, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="images/users", blank=True, null=True)
    intro = models.TextField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return self.username
