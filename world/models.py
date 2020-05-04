from django.db import models

# Create your models here.


# Countries which are available for selection.
class Country(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, unique=True)
    abbreviation = models.CharField(max_length=3, unique=True)
    flag = models.ImageField(upload_to="images/countries", blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


# Country Subdivisions which are available for selection.
class State(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=3)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
