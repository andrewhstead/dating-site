# Generated by Django 2.2.4 on 2019-09-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0017_auto_20190906_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='blocked',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
