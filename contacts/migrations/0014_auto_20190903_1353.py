# Generated by Django 2.2.4 on 2019-09-03 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_auto_20190902_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='p1_messages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='interaction',
            name='p2_messages',
            field=models.IntegerField(default=0),
        ),
    ]
