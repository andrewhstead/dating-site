from django.contrib import admin
from .models import User, Ethnicity, Hair, Eyes, Gender, Relationship, \
    MaritalStatus, Denomination, Diet, Drinks, Smokes, HasChildren, WantsChildren

# Register your models here.
admin.site.register(User)
admin.site.register(Ethnicity)
admin.site.register(Hair)
admin.site.register(Eyes)
admin.site.register(Gender)
admin.site.register(Relationship)
admin.site.register(MaritalStatus)
admin.site.register(Denomination)
admin.site.register(Diet)
admin.site.register(Drinks)
admin.site.register(Smokes)
admin.site.register(HasChildren)
admin.site.register(WantsChildren)
