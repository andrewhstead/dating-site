# Generated by Django 2.2.4 on 2019-09-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20190903_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='p1_last_message',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='interaction',
            name='p2_last_message',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
