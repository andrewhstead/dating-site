# Generated by Django 2.2.4 on 2019-09-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190815_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_active',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
