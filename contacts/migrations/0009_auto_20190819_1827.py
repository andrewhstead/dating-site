# Generated by Django 2.2.4 on 2019-08-19 17:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0008_view'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='View',
            new_name='ProfileView',
        ),
    ]
