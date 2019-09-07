# Generated by Django 2.2.4 on 2019-09-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_message_interaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='p1_has_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interaction',
            name='p2_has_blocked',
            field=models.BooleanField(default=False),
        ),
    ]